import os
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
if __name__ == '__main__':

    test_name = 'data/test.txt'
    train_name = 'data/train.txt'
    dev_name = 'data/dev.txt'

    train = pd.read_table(train_name,sep='\t',error_bad_lines=False)
    test = pd.read_table(test_name, sep='\t', error_bad_lines=False)
    dev = pd.read_table(dev_name, sep='\t', error_bad_lines=False)


    sources = train.iloc[:,0].values
    source_set = set()
    source_all = set()
    for source in sources:
        if isinstance(source,float):
            continue
        source_list = source.split()
        for source_item in source_list:
            source_set.add(source_item.lower())
            source_all.add(source_item.lower())


    sources_test = test.iloc[:,0].values
    source_set_test = set()
    for source in sources_test:
        source_list = source.split()
        for source_item in source_list:
            source_set_test.add(source_item.lower())
            source_all.add(source_item.lower())


    sources_dev = dev.iloc[:,0].values
    source_set_dev = set()
    for source in sources_dev:
        source_list = source.split()
        for source_item in source_list:
            source_set_dev.add(source_item.lower())
            source_all.add(source_item.lower())


    print('='*15,'source')
    print(len(source_set))
    print(len(source_set_test))
    print(len(source_set_dev))
    print('all',len(source_all))



    Target = train.iloc[:,1].values
    target_set = set()
    target_all = set()
    for target in Target:
        if isinstance(target,float):
            continue
        target_list = target
        for target_item in target_list:
            target_set.add(target_item)
            target_all.add(target_item)


    target_test = test.iloc[:,1].values
    target_set_test = set()
    for target in target_test:
        if isinstance(target,float):
            continue
        target_list = target
        for target_item in target_list:
            target_set_test.add(target_item)
            target_all.add(target_item)


    target_dev = dev.iloc[:,1].values
    target_set_dev = set()
    for target in target_dev:
        if isinstance(target,float):
            continue
        target_list = target
        for target_item in target_list:
            target_set_dev.add(target_item)
            target_all.add(target_item)

    print('=' * 15, 'target')
    print(len(target_set))
    print(len(target_set_test))
    print(len(target_set_dev))
    print('all',len(target_all))
