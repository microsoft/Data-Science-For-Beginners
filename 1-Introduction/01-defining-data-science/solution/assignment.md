# Assignment: Data Science Scenarios

In this first assignment, we ask you to think about some real-life process or problem in different problem domains, and how you can improve it using the Data Science process. Think about the following:

1. Which data can you collect?
1. How would you collect it?
1. How would you store the data? How large the data is likely to be?
1. Which insights you might be able to get from this data? Which decisions we would be able to take based on the data?

Try to think about 3 different problems/processes and describe each of the points above for each problem domain.

Here are some of the problem domains and problems that can get you started thinking:

1. How can you use data to improve education process for children in schools?
1. How can you use data to control vaccination during the pandemic?
1. How can you use data to make sure you are being productive at work?
## Instructions

Fill in the following table (substitute suggested problem domains for your own ones if needed):

| Problem Domain | Problem | Which data to collect | How to store the data | Which insights/decisions we can make | 
|----------------|---------|-----------------------|-----------------------|--------------------------------------|
| Education | In university, we typically have low attendance to lectures, and we have the hypothesis that students who attend lectures on average to better during exams. We want to stimulate attendance and test the hypothesis. | We can track attendance through pictures taken by the security camera in class, or by tracking bluetooth/wifi addresses of student mobile phones in class. Exam data is already available in the university database. | In case we track security camera images - we need to store a few (5-10) photographs during class (unstructured data), and then use AI to identify faces of students (convert data to structured form). | We can compute average attendance data for each student, and see if there is any correlation with exam grades. We will talk more about correlation in [probability and statistics](../../04-stats-and-probability/README.md) section. In order to stimulate student attendance, we can publish the weekly attendance rating on school portal, and draw prizes among those with highest attendance. |
| Vaccination | | | | |
| Productivity | | | | |

> *We provide just one answer as an example, so that you can get an idea of what is expected in this assignment.*

## Rubric

Exemplary | Adequate | Needs Improvement
--- | --- | -- |
One was able to identify reasonable data sources, ways of storing data and possible decisions/insights for all problem domains | Some of the aspects of the solution are not detailed, data storage is not discussed, at least 2 problem domains are described | Only parts of the data solution are described, only one problem domain is considered.
