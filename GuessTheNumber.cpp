#include <iostream>
#include <conio.h>

int main(void)
{
	char username[10000];
	srand((unsigned)time(NULL));
	int randnum = rand() % 20 + 1; // (1,20)
	int usernum = -1;
	cout << "Hello! What is your name?" << endl;
	cin >> username;
	cout << "Well, " << username << ", I am thinking of a number between 1 and 20" << endl;
	int trynum = 1;

	while(randnum != usernum && trynum <= 6)
	{
		cout << "Take a guess" << endl;
		cin >> usernum;
		if(usernum < randnum){
			cout << "Your guess is too low" << endl;
		}
		else if(usernum > randnum){
			cout << "Your guess is too high" << endl;
		}
		else if(usernum == randnum){
			break;
		}
		trynum++;
	}
	if(usernum == randnum) {
		cout << "Good job, " << username << "! you guessed my number in " << trynum << " guesses!" << endl;
	}
	else if(usernum != random) {
		cout << "Nope. The number I was thinking of was " << randnum << endl;
	}
}