#!/usr/bin/python3.6
# created by cicek on 14.09.2018 23:05

a = 20
for i in range(1, a):
    print(("\t\t   " + " "*(a-i)) + ("/"*i) + ("\\"*i))

print("\t\t   " + "/"*(a-7) + "G O O D B Y E" + "\\"*(a-6))

b = 31
for i in range(21, b):
    print((" "*(b-i)) + ("/"*i) + ("\\"*i))

# output:
'''
                              /\
                             //\\
                            ///\\\
                           ////\\\\
                          /////\\\\\
                         //////\\\\\\
                        ///////\\\\\\\
                       ////////\\\\\\\\
                      /////////\\\\\\\\\
                     //////////\\\\\\\\\\
                    ///////////\\\\\\\\\\\
                   ////////////\\\\\\\\\\\\
                  /////////////\\\\\\\\\\\\\
                 //////////////\\\\\\\\\\\\\\
                ///////////////\\\\\\\\\\\\\\\
               ////////////////\\\\\\\\\\\\\\\\
              /////////////////\\\\\\\\\\\\\\\\\
             //////////////////\\\\\\\\\\\\\\\\\\
            ///////////////////\\\\\\\\\\\\\\\\\\\
           /////////////G O O D B Y E\\\\\\\\\\\\\\
          /////////////////////\\\\\\\\\\\\\\\\\\\\\
         //////////////////////\\\\\\\\\\\\\\\\\\\\\\
        ///////////////////////\\\\\\\\\\\\\\\\\\\\\\\
       ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\
      /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
     //////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\
    ///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
   ////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  /////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 //////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

'''
