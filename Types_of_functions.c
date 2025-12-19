//no_argument_without_return_type
//1.
#include<stdio.h>
void sum(void);
void main()
{
    sum();
}
void sum()
{
    int a=3,b=4,sum=0;
    sum = a+b;
    printf("sum = %d\n",sum);
}


//2.subtraction;
#include<stdio.h>
void sub(void);
void main()
{
    sub();
    sub();
}
void sub()
{
    int a=10,b=5,sub=0;
    sub = a-b;
    printf("The difference of two numbers is %d\n",sub);
}


//No_argument_with_return_type
//3.
#include<stdio.h>
int sum(void);
void main()
{
    int s;
    s = sum();
    s = sum();
    printf("The sum of two numbers is %d\n",s);

}
int sum()
{
    int a,b,sum =0;
    printf("Enter the value of 'a' and 'b': \n");
    scanf("%d %d",&a,&b);
    sum = a+b;
    return sum;

}
////////////////////////////or\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
//4.
#include<stdio.h>
int sum(void);
void main()
{
    sum();
    sum();
    sum();


}
int sum()
{
    int a,b,sum =0;
    printf("Enter the value of 'a' and 'b': \n");
    scanf("%d %d",&a,&b);
    sum = a+b;
    printf("The sum of two numbers is %d\n",sum);
    return sum;

}
//5.
#include<stdio.h>
char sum(void);
void main()
{
    char s;
    s = sum();
    printf("Sum =%d\n",s);
}
char sum()
{
    char a = 2,b = 3,sum = 0;
    sum = a+b;
    return sum;
    printf("hi");
}
*/


