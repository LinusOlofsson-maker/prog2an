#include <cstdlib>
// *Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib(age);
	private:
		int age;
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}

int Person::fib(){
	int n = age;
	if int(n <= 1)
		return n
	return fib(n - 1) + fib(n - 2)
}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}