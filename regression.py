import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def costFunction(X,y,theta):
        
        s=X*theta[1][0]+theta[0][0]

        s=(s-y)**2
        
        s=sum(s)
        
        s=s/float((2*len(X)))
        
        return s


def gradientDecent(X,y,thetha,alpha=0.0001,itrations=10000):
        
        m=len(X)
        
        temp1=thetha[0][0]
        temp2=thetha[1][0]
        
        for i in range(itrations):

                a=alpha*(float(1)/float(m))*sum(((X*temp2+temp1) - y))
                b=alpha*(float(1)/float(m))*sum(((X*temp2+temp1) - y)*X)
                
                a = float(temp1 - a)
                b = float(temp2 - b)

                temp1=a
                temp2=b
                #print a,b

        print "cost : " ,str(costFunction(X,y,[[a],[b]]))  
        return a,b


def regGraph(X,y,thetha):
        
        plt.scatter(X,y,label='scatter plot',c='#ef5423')
        
        y1=thetha[0][0]+thetha[1][0]*X
        plt.plot(X,y1,label='regression line',color='#58b970')
        
        plt.title("Linear Regression")
        plt.legend()
        plt.show()

        

def main():
        
        f=pd.read_csv('data.csv')
        
        X=np.array([],np.float64)               #input
        y=np.array([],np.float64)               #output
        thetha=np.array([[0],[0]],np.float64)   #slope and intercept
        
        X=f['X']                                #extracting input colomn
        y=f['Y']                                #extracting output colomn
        
        print "training................"
        a,b=gradientDecent(X,y,thetha)          
        
        thetha[0][0]=float(a)
        thetha[1][0]=float(b)
        
        print 'slop : {}\nintercept: {}'.format(a,b)

        regGraph(X,y,thetha)

        

if __name__=='__main__':
        main()


