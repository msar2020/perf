import sys
sys.path.insert(0,'../')
print(sys.path)
import timeit
from timeit import Timer
import bsearch
from bsearch import binary_search
import copy
perfLIST = []
measure_param = [100000,1100001,100000]
def test_odd_len_res_True():
    assert binary_search([0,3,4,26,52,90,99,120,123],99) == True
def test_even_len_res_True():
    assert binary_search([0,3,4,26,52,90,96,99,120,123],0) == True
def test_odd_len_res_False():
    assert binary_search([0,3,4,26,52,90,99,120,123],1345) == False
def test_even_len_res_False():
    assert binary_search([0,3,4,26,52,90,96,99,120,123],-1) == False


# code snippet to be executed only once

# timeit statement



def atest_perf_search_rec():
    bcList = []
    for i in range(measure_param[0],measure_param[1],measure_param[2]):

        SETUP_CODE = '''
from bsearch import binary_search
from random import randint'''
        for find in [i//2 , i - 1 , -1]:
            TEST_CODE = '''
mylist = [x for x in range(%d)]
binary_search(mylist,%d)'''%(i,find)


            bc = (timeit.timeit(setup = SETUP_CODE,
                                    stmt = TEST_CODE,
                                    number = 1000))
            print('The Parameters of the test are find : %d - length %d - Time : %f'%(find,i,bc))

            bcList.append(bc)


    print(bcList)

    '''
# bc is best case, wc is worst case , unk is search failed case
data_bc = [i for ind,i in enumerate(bcList) if ind%3 == 0]
data_wc = [i for ind,i in enumerate(bcList) if ind%3 == 1]
data_unk = [i for ind,i in enumerate(bcList) if ind%3 == 2]
x = range(0, len(bc) // 3)
import matplotlib.pyplot as plt
plt.plot(x, data_bc, label="Match - BestCase")
plt.plot(x, data_wc, label="Match - WorstCase")
plt.plot(x, data_unk, label="NoMatch - WorstCase")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, data_unk, 1))(np.unique(x)), label ="Fit")
plt.plot()
plt.xlabel("Samples")
plt.ylabel("Time in secs from timeit")
plt.title("compare time in secs vs Binary search algorithm")
plt.legend()
plt.show()
    '''


def atest_perf_search_while():
    bcList = []
    global perfLIST
    print(perfLIST)

    for i in range(measure_param[0],measure_param[1],measure_param[2]):
        SETUP_CODE = '''
from bsearch import binary_search1
from random import randint'''
        TEST_CODE = '''
mylist = [x for x in range(%d)]
find = randint(0, len(mylist))
binary_search1(mylist,find)'''%i
        bc = (timeit.timeit(setup = SETUP_CODE,
                                stmt = TEST_CODE,
                                number = 1000))

        bcList.append(bc)
    if len(perfLIST):
        assert True, 'Nothing to compare - Passed'
    else:
        print(bcList,perfLIST)
    return bcList


def test_perf_search_rec1():
    global perfLIST
    bcList = []
    print(perfLIST)
    for i in range(measure_param[0],measure_param[1],measure_param[2]):

        SETUP_CODE = '''
from bsearch import binary_search
from random import randint'''
        for find in [i//2 , i - 1 , -1]:
            TEST_CODE = '''
binary_search(0,%d,%d)'''%(i,find)


            bc = (timeit.timeit(setup = SETUP_CODE,
                                    stmt = TEST_CODE,
                                    number = 1000))
            print('The Parameters of the test are find : %d - length %d - Time : %f'%(find,i,bc))

            bcList.append(bc)


    print(bcList)
