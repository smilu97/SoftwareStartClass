#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

enum {NOEXIST = 0, EXIST};
#define INFINITE 9999999

vector< vector<int> > rn; // Road Network Matrix
int numOfVertices; // the number of vertices
int numOfRoads; // the number of roads

bool isRoadEmpty()
{
	for(int i=0;i<numOfVertices;++i) for(j=0;j<numOfVertices;++j) {
		if(rn[i][j] == EXIST) return false;
	}
	return true;
}

vector<int> tracker;
bool DFSEuler(int position)
{
	tracker.push_back(position);
	if(tracker.size() == numOfRoads) {
		return true;
	}
	for(int dest=0; dest<numOfVertices; ++dest) {
		if(dest == position) continue;
		if(rn[position][dest] == EXIST) {
			rn[position][dest] = NOEXIST;
			rn[dest][position] = NOEXIST;
			bool finded = DFSEuler(dest);
			rn[position][dest] = EXIST;
			rn[dest][position] = EXIST;
			if(finded) {
				return true;
			}
		}
	}
	tracker.pop_back();
	return false;
}

int main(int argc, char **argv)
{
	cin >> numOfVertices >> numOfRoads;
	rn.resize(numOfVertices);
	for(int i=0; i < numOfVertices; ++i) {
		rn[i].resize(numOfVertices, NOEXIST);
	}
	for(int i=0; i < numOfRoads; ++i) {
		int from, to;
		cin >> from >> to;
		from--;
		to--;
		rn[from][to] = EXIST
		rn[to][from] = NOEXIST
	}
	tracker.reserve(1000);
	for(int i=0;i<numOfVertices; ++i) {
		tracker.clear();
		if(DFSEuler(i)) break;
	}
	for(int i=0;i<tracker.size(); ++i) {
		cout << tracker[i] << " ";
	}
	cout << endl;
	return 0;
}