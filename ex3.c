#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
typedef int ll;
typedef double d;
#define K 5
d data[320][690];
d core[20][690];
d dist(ll x,ll y){
    d otc=0;
    for(ll i=0;i<690;i++){
        d gap=data[x][i]-core[y][i];
        otc+=gap*gap;
    }
    return sqrt(otc);
}
int main(){
    FILE*xx=fopen("data.txt","r");
    for(ll i=0;i<320;i++)for(ll j=0;j<690;j++)fscanf(xx,"%lf",&data[i][j]);
    fclose(xx);
    for(ll loop=10;loop;loop--){
    srand(time(NULL));
    for(ll i=0;i<K;i++){
        ll row=rand()%320;
        for(ll j=0;j<690;j++)core[i][j]=data[row][j];
    }
    for(ll l=0;;l++){
        //printf("%d--\n",l);
        d temp[K][690]={.0},var=.0;ll ct[K]={0},flag=0;
        for(ll i=0;i<320;i++){
            d min=10000;ll pos=0;
            for(ll j=0;j<K;j++){
                d tem=dist(i,j);
                if(min>tem)min=tem,pos=j;
            }
            for(ll j=0;j<690;j++)temp[pos][j]+=data[i][j];
            var+=min*min;
            ct[pos]++;
        }
        for(ll i=0;i<K;i++)
            for(ll j=0;j<690;j++){
                temp[i][j]/=ct[i];
                if(temp[i][j]!=core[i][j])core[i][j]=temp[i][j],flag=1;
            }
        if(!flag||l>=600/K){printf("%lf\n",var);break;}
    }
    sleep(2);
    }
}