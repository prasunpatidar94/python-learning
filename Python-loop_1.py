{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/prasunpatidar94/python-learning/blob/main/Python-loop_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## For loop :\n"
      ],
      "metadata": {
        "id": "meiY2ZzQHjCa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# For loop in other progamming\n",
        "for(int i=0 , i<10,i++):\n",
        "  print(\"data :\", i)"
      ],
      "metadata": {
        "id": "mqYSiRrJHsrh",
        "outputId": "ed96cea5-7a33-4b60-ceec-f44f62eccac2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        }
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax. Perhaps you forgot a comma? (4268536387.py, line 2)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_8916/4268536387.py\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    for(int i=0 , i<10,i++):\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# python For Loop:\n",
        "for i in range(10):\n",
        "  print(\"data\",i)"
      ],
      "metadata": {
        "id": "FVSfKg8CIX9Z",
        "outputId": "a891b919-75c5-4963-e872-bf049dabbd95",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "data 0\n",
            "data 1\n",
            "data 2\n",
            "data 3\n",
            "data 4\n",
            "data 5\n",
            "data 6\n",
            "data 7\n",
            "data 8\n",
            "data 9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# for type 2\n",
        "for i in range(0,10):\n",
        "  print(\"data : \",i)"
      ],
      "metadata": {
        "id": "pvd_q5fUIbO0",
        "outputId": "d32384a2-ecb7-4e02-8660-f9fd16c6e541",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "data :  0\n",
            "data :  1\n",
            "data :  2\n",
            "data :  3\n",
            "data :  4\n",
            "data :  5\n",
            "data :  6\n",
            "data :  7\n",
            "data :  8\n",
            "data :  9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# for look 3rd type :\n",
        "for i in range(1,10,3):\n",
        "  print(\"data : \",i)\n",
        ""
      ],
      "metadata": {
        "id": "1Y7yC8WlJANZ",
        "outputId": "347b52f0-768e-45a4-eb8a-d58a68b0877a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "data :  1\n",
            "data :  4\n",
            "data :  7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5,-10,-2):\n",
        "  print(\"data : \", i ,end=\", \")"
      ],
      "metadata": {
        "id": "QW1yGltMKfwN",
        "outputId": "82dd22c4-f61a-4bbd-d242-3736445c6c20",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "data :  5, data :  3, data :  1, data :  -1, data :  -3, data :  -5, data :  -7, data :  -9, "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# for loop 4th type with sequence\n",
        "for i in [1,2,3,4,5,6,7,4,3,21]:\n",
        "  print(\"data : \",i,end=\", \")\n",
        "\n",
        "print()\n",
        "for i in (1,2,3,4,5,6,7,4,3,21):\n",
        "  print(\"data : \",i,end=\", \")\n",
        "\n",
        "print()\n",
        "for i in {1,2,3,4,5,6,7,4,3,21}:\n",
        "  print(\"data : \",i,end=\", \")\n",
        "\n",
        "print()\n",
        "for i in \"Prasun Patidar\":\n",
        "  print(i,end=\"|\")\n"
      ],
      "metadata": {
        "id": "45Y5UMS6JSG-",
        "outputId": "9cc5dbd7-edc7-464c-b138-0ff81211c7f2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "data :  1, data :  2, data :  3, data :  4, data :  5, data :  6, data :  7, data :  4, data :  3, data :  21, \n",
            "data :  1, data :  2, data :  3, data :  4, data :  5, data :  6, data :  7, data :  4, data :  3, data :  21, \n",
            "data :  1, data :  2, data :  3, data :  4, data :  5, data :  6, data :  7, data :  21, \n",
            "P|r|a|s|u|n| |P|a|t|i|d|a|r|"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Nexted For loop:"
      ],
      "metadata": {
        "id": "mbgmOETPMhfS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## right angal Starts\n",
        "\n",
        "rows = int(input(\"Enter the rows value in int\"))\n",
        "\n",
        "for i in range(1,rows):\n",
        "  for j in range(1,i):\n",
        "    print(\"*\", end = \"\")\n",
        "  print()\n",
        "\n",
        "print(\"--------------------------------\")\n",
        "\n",
        "\n",
        "for i in range(1,rows):\n",
        "  for j in range(i,rows):\n",
        "    print(\"*\", end = \"\")\n",
        "  print()\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "zGTSubiCJjTf",
        "outputId": "1bb013c2-5c53-4e26-812b-fa2f2a55887f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the rows value in int10\n",
            "\n",
            "*\n",
            "**\n",
            "***\n",
            "****\n",
            "*****\n",
            "******\n",
            "*******\n",
            "********\n",
            "--------------------------------\n",
            "*********\n",
            "********\n",
            "*******\n",
            "******\n",
            "*****\n",
            "****\n",
            "***\n",
            "**\n",
            "*\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "CwDO_8xtNA2g"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome To Colab",
      "toc_visible": true,
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}