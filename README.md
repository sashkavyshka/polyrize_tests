# How to run the tests

###### Clone the repo.
Clone the repository
`git clone https://github.com/sashkavyshka/polyrize_tests.git`

## magic_list.py: The first assignment
### First option: Run python
```from magic_list import *```
Now you can create objects of type MagicList

### Second option: run the whole file
There is a basic test there:
```
    a = MagicList()
    a[0] = 5
    print(a)
    b = MagicList()
    b[1] = 5
    print(b)
```
The test will print a and fail on b.


## test_api.py: The second assignment

### Run the server.py - so you have what to test
Clone the repository 
`git clone https://github.com/polyrize/interview-server.git`
Run the server according to it's README

### Now we assume that the server is running

To test it, you have test_api.py file. 
It's a pytest file, you can run all of it or test by test.

The list of tests is:

* test_wrong_auth
* test_auth
* test_get
* test_create_obj
* test_get_last_obj
* test_delete_last_obj

Of course it's not a full suite, I didn't have enough time to write a bigger test suite.

So there is only one negative test there and no load testing.

 ## To run
 To run all tests altogether:
 ```pytest test_api.py -s -v```
 
 To run test by test:
```pytest test_api.py::<test_name> -s -v```

They are designed to run separately as well.

## Found bugs
CREATE creates a correct PolyList, but the responce is wrong: the field "data" is named "value" and the field "object_id" is named "id"

So this test is skipped by default.

DELETE deletes the object, but returns a wrong response: 200 instead of 204. So the function is also skipped.
