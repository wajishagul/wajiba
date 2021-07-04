{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Task20.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EkO8agW0afhK"
      },
      "source": [
        "**Create an Employee Table with employee name,employee ID & Salary**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-3GIZe_maUkJ"
      },
      "source": [
        "import mysql.connector\n",
        "\n",
        "mydb = mysql.connector.connect(\n",
        "  host=\"localhost\",\n",
        " user=\"root\",\n",
        "  password=\"1234\",\n",
        ")\n",
        "\n",
        "mycursor = mydb.cursor()\n",
        "print(mydb)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PrNGNPs0atMQ"
      },
      "source": [
        "dbse = mydb.cursor()\n",
        "\n",
        "dbse.execute(\"CREATE DATABASE Employee_Mangement\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Dl70boY-avdf"
      },
      "source": [
        "dbse = mydb.cursor()\n",
        "\n",
        "dbse.execute(\"SHOW DATABASES\")\n",
        "\n",
        "for entry in dbse:\n",
        "    print(entry)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mcRdNygiavjn"
      },
      "source": [
        "mydb = mysql.connector.connect(\n",
        "  host=\"localhost\",\n",
        " user=\"root\",\n",
        "  password=\"1234\",\n",
        "  database=\"employee_mangement\"\n",
        ")\n",
        "dbse = mydb.cursor()\n",
        "\n",
        "dbse.execute(\"CREATE TABLE Employee (emp_id INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oRdPobnHa2i-"
      },
      "source": [
        "dbse = mydb.cursor()\n",
        "\n",
        "dbse.execute(\"SHOW TABLES\")\n",
        "\n",
        "for value in dbse:\n",
        "  print(value)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B-0sQWQNa44a"
      },
      "source": [
        "dbse = mydb.cursor()\n",
        "\n",
        "dbse.execute(\"SHOW COLUMNS FROM employee\")\n",
        "\n",
        "for value in dbse:\n",
        "  print(value)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3sjyderLbASG"
      },
      "source": [
        " **Write a query to get the maximum and minimum salary from employees table**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "szHjHLoca7ml"
      },
      "source": [
        "mycursor = mydb.cursor()\n",
        "\n",
        "mycursor.execute(\"SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select max(EMP_SALARY) from employee)\")\n",
        "\n",
        "myresult = mycursor.fetchall()\n",
        "\n",
        "for x in myresult:\n",
        "    print(x)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nUb4CUwPbImg"
      },
      "source": [
        "mycursor = mydb.cursor()\n",
        "\n",
        "mycursor.execute(\"SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select min(EMP_SALARY) from employee)\")\n",
        "\n",
        "myresult = mycursor.fetchall()\n",
        "\n",
        "for x in myresult:\n",
        "    print(x)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eb6sLlbRbOoT"
      },
      "source": [
        "**Write a query to get the number of employees working with the company**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oXxzrjdIbN6p"
      },
      "source": [
        "mycursor = mydb.cursor()\n",
        "\n",
        "mycursor.execute(\"SELECT COUNT(*) from employee\")\n",
        "\n",
        "myresult = mycursor.fetchall()\n",
        "\n",
        "for x in myresult:\n",
        "    print(x)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FjFboKfFbXDh"
      },
      "source": [
        "**Write a query to get the first 3 characters of first name from employees table**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B-h7XnVPbWQc"
      },
      "source": [
        "mycursor = mydb.cursor()\n",
        "\n",
        "mycursor.execute(\"SELECT * from employee WHERE EMP_NAME LIKE('ANU%')\")\n",
        "\n",
        "myresult = mycursor.fetchall()\n",
        "\n",
        "for x in myresult:\n",
        "    print(x)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}