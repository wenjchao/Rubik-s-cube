#include<iostream>
#include <queue>
using namespace std;

int FINISHED[40] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
int SIDES[12][8];
int blue[8] = {0,7,6,11,18,19,12,8};
int red[8] = {2,1,0,8,12,13,14,9};
int orange[8] = {6,5,4,10,16,17,18,11};
int green[8] = {4,3,2,9,14,15,16,10};
int white[8] = {0,1,2,3,4,5,6,7};
int yellow[8] = {12,19,18,17,16,15,14,13};
int temp;

void set(){
	for(int i = 0 ; i < 8 ; i ++){
		SIDES[ 0 ][ i ] = blue [ i ];
		SIDES[ 1 ][ i ] = blue [ ( 8 - i ) % 8 ];
		SIDES[ 2 ][ i ] = red [ i ];
		SIDES[ 3 ][ i ] = red [ ( 8 - i ) % 8 ];
		SIDES[ 4 ][ i ] = green [ i ];
		SIDES[ 5 ][ i ] = green [ ( 8 - i ) % 8 ];
		SIDES[ 6 ][ i ] = orange [ i ];
		SIDES[ 7 ][ i ] = orange [ ( 8 - i ) % 8 ];
		SIDES[ 8 ][ i ] = white [ i ];
		SIDES[ 9 ][ i ] = white [ ( 8 - i ) % 8 ];
		SIDES[ 10 ][ i ] = yellow [ i ];
		SIDES[ 11 ][ i ] = yellow [ ( 8 - i ) % 8 ];
	}
}

class cube
{
public:
	int state[40];

	cube(){
		for( int i = 0 ; i < 40 ; i ++ ){
			state [ i ] = FINISHED [ i ];
		}
	}

	int turn( int num , int clockwise ){
		return (num + clockwise + 3) % 3;
	}

	int turn( int num ){
		return 1 - num;
	}

	void input(){
		for( int j = 0 ; j < 40 ; j ++ ){
			cin>>state [ j ];
		}
	}

	void spin( int *state, int index ){

		temp = state [ SIDES[ index ][0] ];
		state [ SIDES[ index ][0] ] = state [ SIDES[ index ][6] ];
		state [ SIDES[ index ][6] ] = state [ SIDES[ index ][4] ];
		state [ SIDES[ index ][4] ] = state [ SIDES[ index ][2] ];
		state [ SIDES[ index ][2] ] = temp;

		temp = state [ SIDES[ index ][1] ];
		state [ SIDES[ index ][1] ] = state [ SIDES[ index ][7] ];
		state [ SIDES[ index ][7] ] = state [ SIDES[ index ][5] ];
		state [ SIDES[ index ][5] ] = state [ SIDES[ index ][3] ];
		state [ SIDES[ index ][3] ] = temp;

		if(index < 8){
			temp = state [ SIDES[ index ][0] + 20 ];
			state [ SIDES[ index ][0] + 20 ] = turn( state [ SIDES[ index ][6] + 20 ] , -1 );
			state [ SIDES[ index ][6] + 20 ] = turn( state [ SIDES[ index ][4] + 20 ] , 1 );
			state [ SIDES[ index ][4] + 20 ] = turn( state [ SIDES[ index ][2] + 20 ] , -1 );
			state [ SIDES[ index ][2] + 20 ] = turn( temp , 1 );
		}
		else{
			temp = state [ SIDES[ index ][0] + 20 ];
			state [ SIDES[ index ][0] + 20 ] = state [ SIDES[ index ][6] + 20 ];
			state [ SIDES[ index ][6] + 20 ] = state [ SIDES[ index ][4] + 20 ];
			state [ SIDES[ index ][4] + 20 ] = state [ SIDES[ index ][2] + 20 ];
			state [ SIDES[ index ][2] + 20 ] = temp;
		}

		if( ( (index == 2 || index == 3) || (index == 6 || index == 7) ) ){
			temp = state [ SIDES[ index ][1] + 20 ];
			state [ SIDES[ index ][1] + 20 ] = turn( state [ SIDES[ index ][7] + 20 ] );
			state [ SIDES[ index ][7] + 20 ] = turn( state [ SIDES[ index ][5] + 20 ] );
			state [ SIDES[ index ][5] + 20 ] = turn( state [ SIDES[ index ][3] + 20 ] );
			state [ SIDES[ index ][3] + 20 ] = turn( temp );
		}
		else{
			temp = state [ SIDES[ index ][1] + 20 ];
			state [ SIDES[ index ][1] + 20 ] = state [ SIDES[ index ][7] + 20 ];
			state [ SIDES[ index ][7] + 20 ] = state [ SIDES[ index ][5] + 20 ];
			state [ SIDES[ index ][5] + 20 ] = state [ SIDES[ index ][3] + 20 ];
			state [ SIDES[ index ][3] + 20 ] = temp;
		}

	}

	int fixxx(){

		temp = 0;
		int counting = 0;
		for( int k = 0 ; k < 40 ; k ++ ){
			if( state [ k ] != FINISHED [k] ){
				temp = 1;
				break;
			}
		}
		if( temp == 0 )
			return 0;

		queue<int> waited;
		for(int r = 0 ; r < 40 ; r ++){
			waited.push( state[r] );
		}
		int tempstate[40];

		while (1) {

			for(int r = 0 ; r < 40 ; r ++){
				tempstate[r] = waited.front();
				waited.pop();
			}

			for(int l = 0 ; l < 12 ; l ++){

				spin( tempstate , l );
				counting++;
				if(counting % 100000 == 0)
					cout<<counting<<endl;
				temp = 0;
				for(int t = 0 ; t < 40 ; t ++){
					waited.push( tempstate[t] );
					if (tempstate [t] != FINISHED[t] )
						temp = 1;
				}
				if(temp == 0)
					return counting;
				spin( tempstate , l + 1 - 2*( l % 2 ) );
			}

		}

	}
};

int main(){
	set();
	cube a;
	for (int i = 0 ; i < 40 ; i ++ )
		cout<<a.state[i]<<"  ";
	cout<<endl;
	a.spin(a.state,10);
	a.spin(a.state,1);
	a.spin(a.state,5);
	a.spin(a.state,6);
	a.spin(a.state,10);
	a.spin(a.state,1);
	a.spin(a.state,5);
	a.spin(a.state,6);
	for (int i = 0 ; i < 40 ; i ++ )
		cout<<a.state[i]<<"  ";
		
	cout<<endl;
	cout<<a.fixxx();
	
	return 0;
}
