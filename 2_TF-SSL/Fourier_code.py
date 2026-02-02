#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
using namespace std;

int main()
{
    Mat input = imread("C:\\Users\\dushuang\\Desktop\\lotsfiles\\bhs\\1.jpg",0);
    imshow("input", input);
    //FFT快速算法首先将二维傅里叶变换转换成两个一维傅里叶变换的乘积，然后在对一维傅里叶变换
    //进行快速算法，根据傅里叶变换的性质可以将n个元素的一维离散傅里叶转换为两个n/2个元素的一维离散傅里叶变换
    //同理递归可以转换成m个一维的离散傅里叶变换，为了方便计算，所以要求图像的尺寸为2阶指数（2,4,8,16,32…）的数组计算速度最快，
    //一个数组尺寸是2、3、5的倍数（例如：300 = 5*5*3*2*2）同样有很高的处理效率。 
    int w = getOptimalDFTSize(input.cols);
    int h = getOptimalDFTSize(input.rows);
    Mat padded;
    copyMakeBorder(input, padded, 0, h - input.rows, 0, w - input.cols, BORDER_CONSTANT, Scalar::all(0));
    padded.convertTo(padded, CV_32FC1);//这样可以将三通道转换为一通道
    imshow("padded", padded);//这句代码其实是错误的，因为inshow只能显示8U的图像，32F的图像显示不出来

    //对时域乘以pow(-1,i+j)后在进行傅里叶变换结果是对频域的中心化，当然也可以转换到频域后进行剪切
    for (int i = 0; i < padded.rows; i++)
    {
        float *ptr = padded.ptr<float>(i);
        for (int j = 0; j < padded.cols; j++)
            ptr[j] *= pow(-1, i + j);
    }

    Mat plane[] = { padded, Mat::zeros(padded.size(), CV_32F) };//创建一个Mat型数组来装转换后的数据，因为Fm一般为复数所以需要两个Mat空间进行装填
    Mat complexImg;
    merge(plane, 2, complexImg);//将Mat数组转换成一个二通道的图，第一个通道为待转换图像。
    dft(complexImg, complexImg);//输入图像为二通道，支持原地转换。

    /*****************gaussian*******************/
    Mat gaussianBlur(padded.size(), CV_32FC2);
    Mat gaussianSharpen(padded.size(), CV_32FC2);
    float D0 = 2 * 10 * 10;
    for (int i = 0; i < padded.rows; i++)//这里够将两个高斯图像
    {
        float*p = gaussianBlur.ptr<float>(i);
        float*q = gaussianSharpen.ptr<float>(i);
        for (int j = 0; j < padded.cols; j++)
        {
            float d = pow(i - padded.rows / 2, 2) + pow(j - padded.cols / 2, 2);//这里d表示该点离图像中心的距离
            p[2 * j] = expf(-d / D0);//gaussianBlur的第零通道，expf return float exp.
            p[2 * j + 1] = expf(-d / D0);//gaussianBlur的第一通道

            q[2 * j] = 1 - expf(-d / D0);//gaossianShapen的第零通道
            q[2 * j + 1] = 1 - expf(-d / D0);//gaussianShapen的第一通道
        }
    }
    multiply(complexImg, gaussianBlur, gaussianBlur);//矩阵元素对应相乘，注意，和矩阵相乘区分
    multiply(complexImg, gaussianSharpen, gaussianSharpen);//对两个平面都做高斯乘法（与先求模再做高斯乘法效果一样）
    /***********************将频域显示出来**************************/
    split(complexImg, plane);
    magnitude(plane[0], plane[1], plane[0]);//求模
    plane[0] += Scalar::all(1);//防止有零，避免不能进行log运算
    log(plane[0], plane[0]);//将坐标压缩，以便观察。因为1000与100相差太大不便观察差异，变成2和3之后容易观察。
    normalize(plane[0], plane[0], 1, 0, CV_MINMAX);
    imshow("dft", plane[0]);
    /*********************将处理之后的频域显示出来************************/
    split(gaussianBlur, plane);
    magnitude(plane[0], plane[1], plane[0]);
    plane[0] += Scalar::all(1);
    log(plane[0], plane[0]);
    normalize(plane[0], plane[0], 1, 0, CV_MINMAX);
    imshow("gaussianBlur", plane[0]);

    split(gaussianSharpen, plane);
    magnitude(plane[0], plane[1], plane[0]);
    plane[0] += Scalar::all(1);
    log(plane[0], plane[0]);
    normalize(plane[0], plane[0], 1, 0, CV_MINMAX);
    imshow("gaussianShapen", plane[0]);

    /************************idft*****************************/
    idft(gaussianBlur, gaussianBlur);//输入图像为二通道
    idft(gaussianSharpen, gaussianSharpen);
    split(gaussianBlur, plane);
    magnitude(plane[0], plane[1], plane[0]);//反变换也是求magnitude
    normalize(plane[0], plane[0], 1, 0, CV_MINMAX);
    imshow("idft-gaussianBlur", plane[0]);

    split(gaussianSharpen, plane);
    magnitude(plane[0], plane[1], plane[0]);
    normalize(plane[0], plane[0], 1, 0, CV_MINMAX);
    imshow("idft_gaussianSharpen", plane[0]);

    waitKey();
    return 0;
}