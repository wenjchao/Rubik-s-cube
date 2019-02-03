#include<iostream>
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

	void spin( int index ){

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
};

int main(){
	set();
	cube a;
	for (int i = 0 ; i < 40 ; i ++ )
		cout<<a.state[i]<<"  ";
	cout<<endl;
	a.spin(11);
	for (int i = 0 ; i < 40 ; i ++ )
		cout<<a.state[i]<<"  ";
	cout<<endl;
	return 0;
}
