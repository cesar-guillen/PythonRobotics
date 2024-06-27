
## Project chosen

Name: PythonRobotics

URL: https://github.com/AtsushiSakai/PythonRobotics?tab=License-1-ov-file

Number of lines of code and the tool used to count it: 
Lines: 21244
Tool used: lizard 

Programming language: Python


## Coverage measurement

### Existing tool

We used coverage to meassure the original coverage of the code it was executed with the command: coverage run -m pytest PythonRobotics/tests

<Show the coverage results provided by the existing tool with a screenshot>

![Capture_git](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/466f6d16-4fc8-4ae0-aed9-fe755a5b8c2f)


### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Group member name>

<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

Cesar Guillen Cuñat
Function 1: distance_to_plane()
https://github.com/cesar-guille![Capture_git_2](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/2055c3fe-4613-42bc-86a8-b5eb07adb2bf)
n/PythonRobotics/commit/6682d08985ad1221ab2b5758947519023304ba83

![Uploading Capture_git_2.JPG…]()


Function 2: verify_node()
https://github.com/cesar-guillen/PythonRobotics/commit/6682d08985ad1221ab2b5758947519023304ba83
![Capture_git_3](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/9c25e276-e0d9-4133-a56f-f492806475fd)


Function 3: oscillations_detection()
https://github.com/cesar-guillen/PythonRobotics/commit/f4fbb3e7ffaaf21f17bec6cde614524c579d52e7

![Capture_git_4](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/68e0fa32-4111-41b1-9759-3edfe71ee66a)


Function 4: verify_indez()
https://github.com/cesar-guillen/PythonRobotics/commit/50a252245e4d2de270563782cf87f7008ada2ac6

![Capture_git_5](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/f424d681-8f6c-4e9e-937a-62484121ef43)


Denis Eminov
Function 1: tau_sobol(dim_num)
Link: 
![Capture_git_6](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/88f12681-1950-461c-afc8-ed3ae0562a77)

Function 2: PIDControl(target, current)
Link:

![Capture_git_7](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/9dc44990-eff8-46ba-84f2-5b335fc17d74)


## Coverage improvement

### Individual tests

Cesar Guillen Cuñat

Distance to plane tests: There are 4 tests for this function 2 for each conditional bench of the function.

https://github.com/cesar-guillen/PythonRobotics/commit/6682d08985ad1221ab2b5758947519023304ba83

old: ![Capture_git_9](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/05840ea4-2e64-4ded-9455-8414044e41b8)

New: ![Capture_git_10](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/304f59dc-a483-446c-a366-244ce875c2fa)

The old coverage was 50% because only one of the two branches for this function was tested. With the new improved test cases the branch coverage is increased to 100%. This is because the new tests test for the previously untested conditional branch. 

Verify Node tests: There are a total of 6 tests for this function one for each conditional branch. 

https://github.com/cesar-guillen/PythonRobotics/commit/6682d08985ad1221ab2b5758947519023304ba83

old: ![Capture_git_11](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/a0e8ec3c-8077-44f6-9c1b-24bbe78b6a32)

new: ![Capture_git_12](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/c273b06a-5f01-4549-a901-b44138270913)

The previous function coverage was only 2/6 branches, with the new improved tests the coverage for this function reaches 100%, covering every single possible branch. This is because each test made for this function tests every conditional statement. 

https://github.com/cesar-guillen/PythonRobotics/commit/50a252245e4d2de270563782cf87f7008ada2ac6

verify_node function had 50% brnach coverage with two more tests i was able to cinrease it to 100% 
old: ![Capture_git_18](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/3b32777d-82d9-435d-97d3-70e376a4f82d)


new: ![Capture_git_19](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/5722fee9-2e1a-482d-8e77-21f4bfaa848c)


https://github.com/cesar-guillen/PythonRobotics/commit/50a252245e4d2de270563782cf87f7008ada2ac6


oscillation_detection had 75% branch coverage an di wa sable to increaes it to 100% 
old: ![Capture_git_20](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/f71a927f-e7ca-4135-b92c-439425bdb3bf)


new:![Capture_git_21](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/b97e61e1-7410-486e-923b-1e387c32c7db)


Denis Eminov
Tau_sobol:
https://github.com/cesar-guillen/PythonRobotics/commit/5a6f5a1eb5188db2df85cb2d848c3b6fb67eacbd
Old:
The older one had a coverage of 0%. Basically, there was no coverage at all for this function.

old: ![Capture_git_13](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/d28732d3-78da-4461-b1c4-2186ec1b3e0b)

new : ![Capture_git_14](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/10f24b4f-062f-4135-9262-05f881022a8f)

In the previous version, the function was not tested at all. That is why it had 0% coverage. With the newly added tests, the coverage now is 100% because all of the possible conditional branches are tested. 

PIDControl:
https://github.com/cesar-guillen/PythonRobotics/commit/5a6f5a1eb5188db2df85cb2d848c3b6fb67eacbd
Old:
The older one had a coverage of 83%. It was significantly higher than the previous one but we wanted to maximize this function’s coverage to 100% as well.

old: ![Capture_git_15](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/3a6579f7-8e52-4b4e-b8c5-232db5bd0a60)

new : ![Capture_git_16](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/266146f6-5867-40f0-bcb3-4125af2adfaa)


## Overall

old: ![Capture_git](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/466f6d16-4fc8-4ae0-aed9-fe755a5b8c2f)
new: ![Capture_git_17](https://github.com/cesar-guillen/PythonRobotics/assets/91685879/815c959b-c6b9-412f-b8f8-e77b89d40819)


## Statement of individual contributions

Statement of individual contributions


Cesar Guillen Cuñat: I first started by creating my own branch on github, after this I created a new test file to test the functions I chose.  I added branch ID’s for every conditional branch inside the functions and made tests that would test those functions and reach those branches. After creating tests to reach every branch I created more tests to test the output of the functions and verify that they were indeed correct. After verifying that the coverage was indeed improved i submitted a pull request and merged with the main branch. 

Denis Eminov: Firstly, I followed the good practices of GitHub by creating my own branch. Afterward, I chose my functions and created the coverage tracker file. I inserted the branch coverage dictionaries for each function and imported them respectively. I saw which conditional branches were not tested in the coverage report. I created my own test file where I wrote the uncovered branches for each function. I also added additional ones just to check the correctness of the functions. After that I ran the coverage tool again and verified that the coverage has increased for each file. At the end, I made a pull request and waited one of my teammates to accept it. I also had to do 2 more function do to our other teammate leaving the group the same day as the deadline

Deveney Campagne: At first I created a new branch, so I could push my changes without interrupting my teammates their progress. After this I executed the coverage test to see which functions had a low branch coverage to see what I could choose. After I chose the functions, I started implementing the given instrumentation in the file of the functions I chose. I also created my own test file and added tests for the branches which weren’t tested. For the instrumentation part where we needed to create data structures, I created a separate file and imported this file with the data structures inside the files on which I was running the tests. With the tests I added, the branch coverage indeed improved. At last, I submitted a pull request, which one of my teammates accepted.

