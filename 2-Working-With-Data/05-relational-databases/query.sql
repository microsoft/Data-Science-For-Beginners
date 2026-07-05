SELECT emp.ENAME, dept.DNAME, proj.PROJID, Managers.Manager
FROM dept
INNER JOIN emp
  on dept.DEPTNO = emp.DEPTNO
INNER JOIN proj
  ON emp.EMPNO = proj.EMPNO
INNER JOIN Managers
  ON Managers.Employee = emp.ENAME
