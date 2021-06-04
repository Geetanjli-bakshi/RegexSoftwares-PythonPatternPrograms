{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "53646732",
   "metadata": {},
   "source": [
    "# 1"
   ]
  },
  {
   "cell_type": "raw",
   "id": "fb2e9383",
   "metadata": {},
   "source": [
    "5 5 5 5 5\n",
    "5 5 5 5\n",
    "5 5 5\n",
    "5 5\n",
    "5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "14a92b2c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 5 5 5 5 \n",
      "5 5 5 5 \n",
      "5 5 5 \n",
      "5 5 \n",
      "5 \n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    for j in range(0,5-i):\n",
    "      print('5',end=' ')\n",
    "    print()\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7c4133a",
   "metadata": {},
   "source": [
    "# 2"
   ]
  },
  {
   "cell_type": "raw",
   "id": "3bc1b0d5",
   "metadata": {},
   "source": [
    "0 1 2 3 4 5\n",
    "0 1 2 3 4\n",
    "0 1 2 3\n",
    "0 1 2\n",
    "0 1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1c8a008d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 2 3 4 5 \n",
      "0 1 2 3 4 \n",
      "0 1 2 3 \n",
      "0 1 2 \n",
      "0 1 \n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    for j in range(0,6-i):\n",
    "        print(j,end=\" \")\n",
    "    print()\n",
    "   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3781cdcf",
   "metadata": {},
   "source": [
    "# 3"
   ]
  },
  {
   "cell_type": "raw",
   "id": "531c4bd9",
   "metadata": {},
   "source": [
    "1\n",
    "3 3\n",
    "5 5 5\n",
    "7 7 7 7\n",
    "9 9 9 9 9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8a50b4ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "3 3 \n",
      "5 5 5 \n",
      "7 7 7 7 \n",
      "9 9 9 9 9 \n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    for j in range(0,i+1):\n",
    "        print(2*i+1,end=' ')\n",
    "    print()\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a398039",
   "metadata": {},
   "source": [
    "# 4"
   ]
  },
  {
   "cell_type": "raw",
   "id": "2233834b",
   "metadata": {},
   "source": [
    "1\n",
    "2 1\n",
    "3 2 1\n",
    "4 3 2 1\n",
    "5 4 3 2 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "64cd2cf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "2 1 \n",
      "3 2 1 \n",
      "4 3 2 1 \n",
      "5 4 3 2 1 \n"
     ]
    }
   ],
   "source": [
    "for i in range(1,6):\n",
    "    for j in range(i,0,-1):\n",
    "        print(j,end=' ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97bf008f",
   "metadata": {},
   "source": [
    "# 5"
   ]
  },
  {
   "cell_type": "raw",
   "id": "9f60ab5b",
   "metadata": {},
   "source": [
    "1\n",
    "3 2\n",
    "6 5 4\n",
    "10 9 8 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "3a81c68c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "3 2 \n",
      "6 5 4 \n",
      "10 9 8 7 \n"
     ]
    }
   ],
   "source": [
    "a=1\n",
    "b=2\n",
    "c=b\n",
    "for i in range(2,6):\n",
    "    for j in range(a,b):\n",
    "        c-=1\n",
    "        print(c, end=' ')\n",
    "    print()\n",
    "    a=b\n",
    "    b+=i\n",
    "    c=b\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3b982a9",
   "metadata": {},
   "source": [
    "# 6"
   ]
  },
  {
   "cell_type": "raw",
   "id": "58fd2bcc",
   "metadata": {},
   "source": [
    "1\n",
    "1 1\n",
    "1 2 1\n",
    "1 3 3 1\n",
    "1 4 6 4 1\n",
    "1 5 10 10 5 1\n",
    "1 6 15 20 15 6 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "08d5bc3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "1 1 \n",
      "1 2 1 \n",
      "1 3 3 1 \n",
      "1 4 6 4 1 \n",
      "1 5 10 10 5 1 \n",
      "1 6 15 20 15 6 1 \n"
     ]
    }
   ],
   "source": [
    "for i in range(0,7):\n",
    "    for j in range(0,i+1):\n",
    "        c=1\n",
    "        if(j>i-j):\n",
    "            j=i-j\n",
    "        for k in range(0,j):\n",
    "            c=c*(i-k)\n",
    "            c=c//(k+1)\n",
    "        print(c,end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "49d2f2a5",
   "metadata": {},
   "source": [
    "# 7"
   ]
  },
  {
   "cell_type": "raw",
   "id": "e8da5f61",
   "metadata": {},
   "source": [
    "1 2 3 4 5\n",
    "2 2 3 4 5\n",
    "3 3 3 4 5\n",
    "4 4 4 4 5\n",
    "5 5 5 5 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "e6d92561",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 \n",
      "2 2 3 4 5 \n",
      "3 3 3 4 5 \n",
      "4 4 4 4 5 \n",
      "5 5 5 5 5 \n"
     ]
    }
   ],
   "source": [
    "for i in range(1,6):\n",
    "    for j in range(1,6):\n",
    "        if j<=i:\n",
    "            print(i,end=' ')\n",
    "        else:\n",
    "            print(j,end=' ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ae9661b",
   "metadata": {},
   "source": [
    "# 8"
   ]
  },
  {
   "cell_type": "raw",
   "id": "2a95692a",
   "metadata": {},
   "source": [
    "1\n",
    "2 4\n",
    "3 6 9\n",
    "4 8 12 16\n",
    "5 10 15 20 25\n",
    "6 12 18 24 30 36\n",
    "7 14 21 28 35 42 49\n",
    "8 16 24 32 40 48 56 64"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "332560c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "2 4 \n",
      "3 6 9 \n",
      "4 8 12 16 \n",
      "5 10 15 20 25 \n",
      "6 12 18 24 30 36 \n",
      "7 14 21 28 35 42 49 \n",
      "8 16 24 32 40 48 56 64 \n"
     ]
    }
   ],
   "source": [
    "for i in range(1,9):\n",
    "    for j in range(1,i+1):\n",
    "        print(i*j,end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07126360",
   "metadata": {},
   "source": [
    "# 9"
   ]
  },
  {
   "cell_type": "raw",
   "id": "d621d9a5",
   "metadata": {},
   "source": [
    "        * * * * * *\n",
    "         * * * * *\n",
    "          * * * *\n",
    "           * * *\n",
    "            * *\n",
    "             *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "75cc905e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        * * * * * * \n",
      "         * * * * * \n",
      "          * * * * \n",
      "           * * * \n",
      "            * * \n",
      "             * \n"
     ]
    }
   ],
   "source": [
    "k=2*5-2\n",
    "for i in range(5,-1,-1):\n",
    "    for j in range(k,0,-1):\n",
    "        print(end=' ')\n",
    "    k=k+1\n",
    "    for j in range(0,i+1):\n",
    "            print('*',end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b4e9bbe5",
   "metadata": {},
   "source": [
    "# 10\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "270c7b72",
   "metadata": {},
   "source": [
    "\n",
    "            *\n",
    "           * *\n",
    "          * * *\n",
    "         * * * *\n",
    "        * * * * *\n",
    "       * * * * * *\n",
    "      * * * * * * *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "14c21841",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            * \n",
      "           * * \n",
      "          * * * \n",
      "         * * * * \n",
      "        * * * * * \n",
      "       * * * * * * \n",
      "      * * * * * * * \n"
     ]
    }
   ],
   "source": [
    "m=(2*7)-2\n",
    "for i in range(0,7):\n",
    "    for j in range(0,m):\n",
    "        print(end=\" \")\n",
    "    m=m-1\n",
    "    for j in range(0,i+1):\n",
    "        print('*',end=' ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ac45839",
   "metadata": {},
   "source": [
    "# 11"
   ]
  },
  {
   "cell_type": "raw",
   "id": "8890233e",
   "metadata": {},
   "source": [
    "*\n",
    "* *\n",
    "* * *\n",
    "* * * *\n",
    "* * * * *\n",
    "* * * * * *  \n",
    "\n",
    "* * * * * * \n",
    "* * * * *\n",
    "* * * *\n",
    "* * *\n",
    "* *\n",
    "*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "985bafe0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*  \n",
      "* *  \n",
      "* * *  \n",
      "* * * *  \n",
      "* * * * *  \n",
      "* * * * * *  \n",
      " \n",
      "* * * * * * \n",
      "* * * * * \n",
      "* * * * \n",
      "* * * \n",
      "* * \n",
      "* \n",
      "\n"
     ]
    }
   ],
   "source": [
    "n=6\n",
    "for i in range(0,n):\n",
    "    for j in range(0,i+1):\n",
    "        print(\"*\",end=' ')\n",
    "    print(' ')\n",
    "print(' ')\n",
    "for i in range(n+1,0,-1):\n",
    "    for j in range(0,i-1):\n",
    "        print('*',end=\" \")\n",
    "    print()\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "746aeb1f",
   "metadata": {},
   "source": [
    "# 12"
   ]
  },
  {
   "cell_type": "raw",
   "id": "aecb8b13",
   "metadata": {},
   "source": [
    "*\n",
    "* *\n",
    "* * *\n",
    "* * * *\n",
    "* * * * *\n",
    "* * * *\n",
    "* * *\n",
    "* *\n",
    "*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "db83b6b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*  \n",
      "* *  \n",
      "* * *  \n",
      "* * * *  \n",
      "* * * * *  \n",
      "* * * *  \n",
      "* * *  \n",
      "* *  \n",
      "*  \n",
      " \n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    for j in range(0,i+1):\n",
    "        print('*',end=\" \")\n",
    "    print(' ')\n",
    "for i in range(5,0,-1):\n",
    "    for j in range(0,i-1):\n",
    "        print('*',end=' ')\n",
    "    print(' ')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ce64416",
   "metadata": {},
   "source": [
    "# 13"
   ]
  },
  {
   "cell_type": "raw",
   "id": "a3a052bf",
   "metadata": {},
   "source": [
    "        *\n",
    "      * *\n",
    "    * * *\n",
    "  * * * *\n",
    "* * * * *\n",
    "  * * * *\n",
    "    * * *\n",
    "      * *\n",
    "        *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "6a8f3567",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        * \n",
      "      * * \n",
      "    * * * \n",
      "  * * * * \n",
      "* * * * * \n",
      "  * * * * \n",
      "    * * * \n",
      "      * * \n",
      "        * \n"
     ]
    }
   ],
   "source": [
    "k=2*5-2\n",
    "for i in range(0,4):\n",
    "    for j in range(0,k):\n",
    "        print(end=' ')\n",
    "    k=k-2\n",
    "    for j in range(0,i+1):\n",
    "        print('*',end=' ')\n",
    "    print()\n",
    "k=-1\n",
    "for i in range(4,-1,-1):\n",
    "    for j in range(k,-1,-1):\n",
    "        print(end=\" \")\n",
    "    k=k+2\n",
    "    for j in range(0,i+1):\n",
    "        print('*',end=\" \")\n",
    "    print()\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec58b02f",
   "metadata": {},
   "source": [
    "# 14"
   ]
  },
  {
   "cell_type": "raw",
   "id": "22607bf4",
   "metadata": {},
   "source": [
    "* * * * *\n",
    " * * * *\n",
    "  * * *\n",
    "   * *\n",
    "    *\n",
    "    *\n",
    "   * *\n",
    "  * * *\n",
    " * * * *\n",
    "* * * * *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "caa5a2a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* * * * * \n",
      " * * * * \n",
      "  * * * \n",
      "   * * \n",
      "    * \n",
      "    * \n",
      "   * * \n",
      "  * * * \n",
      " * * * * \n",
      "* * * * * \n"
     ]
    }
   ],
   "source": [
    "row=5\n",
    "i=0\n",
    "while i<=row-1:\n",
    "    j=0\n",
    "    while j<i:\n",
    "        print('',end=' ')\n",
    "        j+=1\n",
    "    k=i\n",
    "    while k <=row-1:\n",
    "        print('*',end=\" \")\n",
    "        k+=1\n",
    "    print()\n",
    "    i+=1\n",
    "i=row-1\n",
    "while i >=0:\n",
    "    j=0\n",
    "    while j<i:\n",
    "        print(\"\",end=' ')\n",
    "        j+=1\n",
    "    k=i\n",
    "    while k<=row-1:\n",
    "        print('*',end=' ')\n",
    "        k+=1\n",
    "    print()\n",
    "    i-=1\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d541a04c",
   "metadata": {},
   "source": [
    "# 15"
   ]
  },
  {
   "cell_type": "raw",
   "id": "df65de42",
   "metadata": {},
   "source": [
    "****************\n",
    "*******__*******\n",
    "******____******\n",
    "*****______*****\n",
    "****________****\n",
    "***__________***\n",
    "**____________**\n",
    "*______________*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "ae34fbb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "**************\n",
      "******--******\n",
      "*****----*****\n",
      "****------****\n",
      "***--------***\n",
      "**----------**\n",
      "*------------*\n"
     ]
    }
   ],
   "source": [
    "n=14\n",
    "print(\"*\"*n,end=\"\\n\")\n",
    "i=(n//2)-1\n",
    "j=2\n",
    "while i !=0:\n",
    "    while j <=(n-2):\n",
    "        print(\"*\"*i,end=\"\")\n",
    "        print('-'*j,end=\"\")\n",
    "        print('*'*i,end=\"\\n\")\n",
    "        i=i-1\n",
    "        j=j+2\n",
    "    \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1881b222",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
