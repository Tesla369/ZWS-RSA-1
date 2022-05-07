#include <iostream>
#include <ctype.h>
#include <cstring>
#include <cstdio>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <unistd.h>
#include <stdio.h>

using namespace std;

void banner(int x)
{
if(x!=1){x+=1;}
else
{
cout<<"\n";
std::cout << '#' << std::flush;
    for (int i=0; i<100; i++) {
        usleep(15000);
        std::cout << "=" << std::flush;
        usleep(15000);
    }
std::cout << '#' << std::flush;    
cout<<"\n\n\n";
cout<<"Version: 1.0\n\n";
//cout<<" ███████████    █████████    █████████              ███████████    █████       █████    ████\n░░███░░░░░███  ███░░░░░███  ███░░░░░███            ░█░░░███░░░█  ███░░░███   ███░░░███ ░░███\n ░███    ░███ ░███    ░░░  ░███    ░███            ░   ░███  ░  ███   ░░███ ███   ░░███ ░███\n ░██████████  ░░█████████  ░███████████  ██████████    ░███    ░███    ░███░███    ░███ ░███\n ░███░░░░░███  ░░░░░░░░███ ░███░░░░░███ ░░░░░░░░░░     ░███    ░███    ░███░███    ░███ ░███\n ░███    ░███  ███    ░███ ░███    ░███                ░███    ░░███   ███ ░░███   ███  ░███\n █████   █████░░█████████  █████   █████               █████    ░░░█████░   ░░░█████░   █████\n░░░░░   ░░░░░  ░░░░░░░░░  ░░░░░   ░░░░░               ░░░░░       ░░░░░░      ░░░░░░   ░░░░░\n";
cout<<" ███████████ █████   ███   █████  █████████             ███████████    █████       █████    ████ \n░█░░░░░░███ ░░███   ░███  ░░███  ███░░░░░███           ░█░░░███░░░█  ███░░░███   ███░░░███ ░░███ \n░     ███░   ░███   ░███   ░███ ░███    ░░░            ░   ░███  ░  ███   ░░███ ███   ░░███ ░███ \n     ███     ░███   ░███   ░███ ░░█████████  ██████████    ░███    ░███    ░███░███    ░███ ░███ \n    ███      ░░███  █████  ███   ░░░░░░░░███░░░░░░░░░░     ░███    ░███    ░███░███    ░███ ░███ \n  ████     █  ░░░█████░█████░    ███    ░███               ░███    ░░███   ███ ░░███   ███  ░███ \n ███████████    ░░███ ░░███     ░░█████████                █████    ░░░█████░   ░░░█████░   █████\n░░░░░░░░░░░      ░░░   ░░░       ░░░░░░░░░                ░░░░░       ░░░░░░      ░░░░░░   ░░░░░ \n                                                                                                 \n                                                                                                 \n                                                                                                 ";
cout<<"\n";
cout<<" 			    +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+\n 			    |P|o|o|r|n|e|s|h| |A|d|h|i|t|h|y|a|\n 			    +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+\n";
cout<<"\n";
std::cout << '#' << std::flush;
    for (int i=0; i<100; i++) {
        usleep(15000);
        std::cout << "=" << std::flush;
        usleep(15000);
    }
std::cout << '#' << std::flush;    
}
}

void welcome()
{
cout<<"\n";
std::cout << '#' << std::flush;
    for (int i=0; i<43; i++) {
        usleep(15000);
        std::cout << "=" << std::flush;
        usleep(15000);
    }
//std::cout << '-' << std::flush;
char bye[20] = {'|',' ','W', 'E', 'L', 'C', 'O', 'M', 'E', '!', '!', '!',' ','|'};
    for (int i=0; bye[i]!='\0'; i++) {
        usleep(15000);
        std::cout << bye[i] << std::flush;
        usleep(15000);
    }

//std::cout << '-' << std::flush;
    for (int i=0; i<43; i++) {
        usleep(15000);
        std::cout << "=" << std::flush;
        usleep(15000);
    }
std::cout << '#' << std::flush;
cout<<"\n\n";
}

void bye()
{
std::cout << '#' << std::flush;
    for (int i=0; i<43; i++) {
        usleep(15000);
        std::cout << "=" << std::flush;
        usleep(15000);
    }
//std::cout << '-' << std::flush;
char bye[20] = {'|',' ','T', 'H', 'A', 'N', 'K', '-', 'Y', 'O', 'U', '!',' ','|'};
    for (int i=0; bye[i]!='\0'; i++) {
        usleep(15000);
        std::cout << bye[i] << std::flush;
        usleep(15000);
    }

//std::cout << '-' << std::flush;
    for (int i=0; i<43; i++) {
        usleep(15000);
        std::cout << "=" << std::flush;
        usleep(15000);
    }
std::cout << '#' << std::flush;
cout<<"\n\n";
}

int powmod(long long x, unsigned int y, int p)
{
int res = 1;
x = x % p;
if (x == 0) return 0;
while (y > 0)
{
if (y & 1)
res = (res*x) % p;
y = y>>1;
x = (x*x) % p;
}

return res;
}

void enc()
{
char pt[100];
long nv[100];
long en[100];
char command[256];
char cmd[256];
long p, q, n, phin, e, gcd;
system("rm -rf secret.txt cover.txt");
cout<<"ENCRYPTION => \n\n";

cout<<"Enter the Secret Text to Encrypt: ";
cin.ignore();
cin.getline(pt, 100);
cout<<"\n\n";
cout<<"Enter the Largest Prime Number, p = ";
cin>>p; //7
cout<<"Enter the Largest Prime Number, q = ";
cin>>q;  //11
cout<<"Enter the Public Key Component, e = ";
cin>>e; //13

char ct[100];
cout<<"\nEnter the Cover Text: ";
cin.ignore();
cin.getline(ct, 100);

snprintf(cmd, 256, "echo -n '%s' >> cover.txt", ct);
system(cmd);

cout<<"\nConfiguring..."<<"\n\n";
usleep(3000000);

phin=(p-1)*(q-1);

n=p*q;

gcd = __gcd(e,phin);

cout<<"Large Prime Numbers:\n";
cout<<"p = "<<p<<"\n";
cout<<"q = "<<q<<"\n\n";
usleep(1000000);
cout<<"n = p x q = "<<n<<"\n";
cout<<"Φ(n) = (p - 1) x (q - 1) = "<<phin<<"\n";
cout<<"Public Key Component (e): "<<e<<"\n";
cout<<"gcd(e, Φ(n)) = "<<"gcd("<<e<<", "<<phin<<") = "<<gcd<<"\n\n";
usleep(1000000);
cout<<"Verifying the following Conditions...\n";
cout<<"1 < e < Φ(n)\n";
cout<<"gcd(e, Φ(n)) = 1\n\n";
usleep(2000000);
if(!((1<e && e<phin) && gcd==1))
{
int t;
cout<<"Conditions not Satisfied.\n";
cout<<"Enter 1 to continue and 0 to exit: ";
cin>>t;
if(t==1)
{
system("clear");
enc();
}
else
{
cout<<"Good Bye!\n\n";
bye();
exit(0);
}
}
cout<<"Conditions Satisfied: \n";
cout<<"1 < e < Φ(n) => "<<"1 < "<<e<<" < "<<phin<<"\n";
cout<<"gcd(e, Φ(n)) = 1 => "<<"gcd("<<e<<", "<<phin<<") = 1\n\n";
usleep(1000000);
cout<<"Plain Text (pt): "<<pt<<"\n";
cout<<"Numerical Value: ";
for(int i=0; pt[i]!='\0'; i++)
{
if(isupper(pt[i]))
{
pt[i] = tolower(pt[i]);
}
//cout<<pt[i];
nv[i] = int(pt[i]) - 97;
cout<<nv[i]<<" ";
}
cout<<"\n";
cout<<"Formula: nv^e mod n\n";
cout<<"Encrypted Cipher Text: ";
for(int i=0; pt[i]!='\0'; i++)
{
en[i] = powmod(nv[i], e, n);
cout<<en[i]<<" ";
snprintf(command, 256, "echo -n '%d ' >> secret.txt", en[i]);
system(command);
//cout<<powmod(nv[i], e, n)<<" ";
//nv[i]=pow(nv[i], e);
//nv[i]=nv[i]%n;
//cout<<nv[i]<<" ";
//system("cat cover.txt");
}

system("python3 zw-stego.py -s secret.txt cover.txt");
cout<<"Cover Text:\n";
system("cat cover.txt");
cout<<"\n\n";
cout<<"Good Bye!\n\n";
}

void dec()
{
string str;
long st[100], nv[100];
long size, p, q, e, n, phin, gcd, k;
double d;
cout<<"DECRYPTION => \n\n";
cout<<"👇 This is Decoded Cipher Text: \n";
str = system("python3 zw-stego.py cover.txt");

cout<<"\nEnter the length of the Cipher Text: ";
cin>>size;
cout<<"\n\n";
str = system("python3 zw-stego.py cover.txt");

cout<<"\nEnter This Cipher Text to Decrypt: ";
for(int i=0; i<size; i++)
{
cin>>st[i];
}


cout<<"\n\n";
cout<<"Enter any Large Prime Number, p = ";
cin>>p; //7
cout<<"Enter any Large Prime Number, q = ";
cin>>q;  //11
cout<<"Enter the Public Key Component, e = ";
cin>>e; //13

cout<<"\nConfiguring..."<<"\n\n";
usleep(3000000);

phin=(p-1)*(q-1);
n=p*q;
gcd = __gcd(e,phin);

cout<<"Large Prime Numbers:\n";
cout<<"p = "<<p<<"\n";
cout<<"q = "<<q<<"\n\n";
usleep(1000000);
cout<<"n = p x q = "<<n<<"\n";
cout<<"Φ(n) = (p - 1) x (q - 1) = "<<phin<<"\n";
cout<<"Public Key Component (e): "<<e<<"\n";
cout<<"gcd(e, Φ(n)) = "<<"gcd("<<e<<", "<<phin<<") = "<<gcd<<"\n\n";
usleep(1000000);
cout<<"Verifying the following Conditions...\n";
cout<<"1 < e < Φ(n)\n";
cout<<"gcd(e, Φ(n)) = 1\n\n";
usleep(2000000);

if(!((1<e && e<phin) && gcd==1))
{
int t;
cout<<"Conditions not Satisfied.\n";
cout<<"Enter 1 to continue and 0 to exit: ";
cin>>t;
if(t==1)
{
system("clear");
dec();
}
else
{
cout<<"Good Bye!\n\n";
bye();
exit(0);
}
}

cout<<"Formula: \n";
cout<<"d = (1 + (k x Φ(n)))/e\n\n";
for(k=1; k>0; k++)
{
d = (1+(k*double(phin)))/double(e);
cout<<"if k = "<<k<<" then, d = (1 + ("<<k<<" x "<<phin<<"))/"<<e<<" = "<<d<<"\n";
if (d == long(d))
{
cout<<"\ntherefore, k = "<<k<<" hence, d = (1 + ("<<k<<" x "<<phin<<"))/"<<e<<" = "<<d;
cout<<"\n";
break;
}
}

cout<<"\n";
cout<<"Formula: ct^d mod n\n";
cout<<"Numerical Value: ";
for(int i=0; i<size; i++)
{
nv[i] = powmod(st[i],d,n);
cout<<nv[i]<<" ";
}

cout<<"\n\n";
cout<<"Plain Text: ";
for(int i=0; i<size; i++)
{
nv[i] = nv[i] + 97;
cout<<char(nv[i]);
}

cout<<"\n\n";

}

void diff()
{

string a, b;
int la;
int lb;
int m=0;
int n=0;
cout<<"\nEnter original text: ";
cin>>a;
cout<<"\nEnter ZWSP cover text: ";
cin>>b;
la = a.length();
lb = b.length();

cout<<"\nLength of original Text: "<<la;
cout<<"\nChars in Original Text: \n";
while (m < la)
{
printf("%2x ", (unsigned char) a[m]);
//printf("%c", a[m]);
m++;
}
printf("\n");

cout<<"\nLength of ZWSP Cover Text: "<<lb;
cout<<"\nChars in ZWSP Cover Text: \n";
while (n < lb)
{
printf("%2x ", (unsigned char) b[n]);
//printf("%c", b[n]);
n++;
}
printf("\n");

if(la == lb)
{
cout<<"\nLength of both the text are same hence there is no difference";
}
else
{
cout<<"\nLength of both the text are different\n";
}

}

void menu()
{
static int x=1;
system("clear");
banner(x);
x+=1;
welcome();
int val;
char ch;
cout<<"ZWS using RSA-1 Algorithm\n\n1. Encryption\n2. Decryption\n3. Difference Checker\n\n0. Exit\n\n\nChoose 1 to Encrypt, 2 to Decrypt, 3 to check difference and 0 to Exit: ";
cin>>val;
if(val==1)
{
cout<<"\n";
enc();
cout<<"\nEnter c to continue to main menu: ";
cin>>ch;
menu();
}
else if(val==2)
{
cout<<"\n";
dec();
cout<<"\nEnter c to continue to main menu: ";
cin>>ch;
menu();
}
else if(val==3)
{
cout<<"\n";
diff();
cout<<"\nEnter c to continue to main menu: ";
cin>>ch;
menu();
}
else
{
cout<<"\n\n";
cout<<"Good Bye!\n\n";
bye();
exit(0);
}
}

int main()
{
//banner();
//welcome();
menu();
//enc();
//dec();
//bye();
}
