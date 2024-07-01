# %%
START TRANSACTION;

INSERT INTO employees (name, position) VALUES ('John Doe', 'Manager');

COMMIT;



# %%
START TRANSACTION;

INSERT INTO employees (name, position) VALUES ('Jane Doe', 'Assistant Manager');

ROLLBACK;


# %%
START TRANSACTION;

INSERT INTO employees (name, position) VALUES ('Alice', 'Developer');

SAVEPOINT savepoint1;

INSERT INTO employees (name, position) VALUES ('Bob', 'Designer');

ROLLBACK TO savepoint1;

COMMIT;


# %%
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

START TRANSACTION;

INSERT INTO employees (name, position) VALUES ('Charlie', 'Analyst');

COMMIT;


# %%
START TRANSACTION;

INSERT INTO employees (name, position) VALUES ('David', 'Architect');

SAVEPOINT savepoint1;

INSERT INTO employees (name, position) VALUES ('Eva', 'Tester');

RELEASE SAVEPOINT savepoint1;

COMMIT;


# %%
CREATE TRIGGER after_employee_insert
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit (employee_id, action, action_time)
    VALUES (NEW.id, 'INSERT', NOW());
END;


# %%
CREATE TRIGGER before_employee_update
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < OLD.salary THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Salary cannot be decreased';
    END IF;
END;


# %%
CREATE TRIGGER after_employee_delete
AFTER DELETE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit (employee_id, action, action_time)
    VALUES (OLD.id, 'DELETE', NOW());
END;


# %%
CREATE TRIGGER before_employee_insert
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    IF NEW.email NOT LIKE '%@%' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid email format';
    END IF;
END;


# %%
CREATE TRIGGER after_employee_update
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit (employee_id, action, action_time)
    VALUES (NEW.id, 'UPDATE', NOW());
END;


# %%
CREATE VIEW employee_view AS
SELECT id, name, position
FROM employees;


# %%
CREATE VIEW employee_department_view AS
SELECT e.id, e.name, d.name AS department
FROM employees e
JOIN departments d ON e.department_id = d.id;

# %%
CREATE VIEW department_salary_view AS
SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY department_id;


# %%
CREATE VIEW employee_salary_view AS
SELECT id, name, salary
FROM employees
WHERE position = 'Developer'
WITH CHECK OPTION;


# %%
CREATE VIEW high_salary_employees AS
SELECT id, name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);


# %%
import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)


# %%
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print("Addition:", c)

d = a * b
print("Multiplication:", d)


# %%
import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

slice_1 = array_2d[0:2, 1:3]
print("Array Slice:\n", slice_1)

# %%
import numpy as np

array_1d = np.array([1, 2, 3, 4, 5, 6])

array_2d = array_1d.reshape((2, 3))
print("Reshaped Array:\n", array_2d)

# %%
import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])

add_array = np.array([1, 1, 1])
result = array_2d + add_array
print("Broadcasting Result:\n", result)

# %%
import numpy as np

array = np.array([1, 4, 9, 16, 25])

sqrt_array = np.sqrt(array)
print("Square Roots:", sqrt_array)


# %%
import numpy as np

array = np.array([1, 2, 3, 4, 5])

mean = np.mean(array)
std_dev = np.std(array)
print("Mean:", mean)
print("Standard Deviation:", std_dev)


# %%
import numpy as np

matrix = np.array([[1, 2], [3, 4]])

determinant = np.linalg.det(matrix)
print("Determinant:", determinant)


# %%
import numpy as np

random_array = np.random.rand(5)
print("Random Array:", random_array)

random_integers = np.random.randint(1, 10, size=5)
print("Random Integers:", random_integers)


# %%
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

concat_axis0 = np.concatenate((a, b), axis=0)
print("Concatenate along axis 0:\n", concat_axis0)

stack_axis1 = np.hstack((a, b))
print("Stack along axis 1:\n", stack_axis1)


# %%
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

result = array[array > 5]
print("Elements greater than 5:", result)

# %%
import numpy as np

array = np.array([10, 20, 30, 40, 50])

indices = [1, 3, 4]
result = array[indices]
print("Fancy Indexing Result:", result)

# %%
import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])

add_array = np.array([1, 1, 1])
result = array_2d + add_array
print("Broadcasting Result:\n", result)



# %%
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)
cross_product = np.cross(a, b)
print("Dot Product:", dot_product)
print("Cross Product:", cross_product)

# %%
import numpy as np

matrix = np.array([[4, -2], [1, 1]])

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)


# %%
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print("DataFrame:\n", df)


# %%
import pandas as pd

df = pd.read_csv('data.csv')
print("Data from CSV:\n", df)

df.to_csv('output.csv', index=False)

# %%
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

age_column = df['Age']
print("Age Column:\n", age_column)

filtered_df = df[df['Age'] > 30]
print("Filtered DataFrame:\n", filtered_df)


# %%
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
        'Age': [25, 30, 35, 28, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles']}
df = pd.DataFrame(data)

grouped = df.groupby('Name').mean()
print("Grouped Data:\n", grouped)


# %%
import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, np.nan, 35],
        'City': ['New York', np.nan, 'Chicago']}
df = pd.DataFrame(data)
print("DataFrame with Missing Values:\n", df)

filled_df = df.fillna({'Age': 30, 'City': 'Unknown'})
print("Filled DataFrame:\n", filled_df)

dropped_df = df.dropna()
print("DataFrame with Missing Values Dropped:\n", dropped_df)

# %%
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Boolean indexing to get elements greater than 5
result = array[array > 5]
print("Elements greater than 5:", result)

# %%



