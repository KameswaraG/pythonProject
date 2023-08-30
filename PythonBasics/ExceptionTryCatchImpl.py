# except will be executed only when test.txt file is not available.


try:
    with open('test.txt') as reader:

        totalContent = reader.readlines()
        print(totalContent)

except:
    print("This block will be executed when an exception occurs")

#except Exception as e:
 #   print(e)
finally:
    print("Irrespective of try & catch this block will be executed for cleaning resources")