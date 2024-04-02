program factorial
   implicit none

   integer :: given_num, reg_num, accumulator
   
   print*,'Enter a number (given_num), I will calculate the factorial'
   read(*,*) given_num
   
   reg_num = 1
   accumulator = 1

   do while ( reg_num <= given_num )
      accumulator = accumulator * reg_num 
      reg_num = reg_num + 1
      print*,'', accumulator
   end do
   print*,'The factorial of the given number', given_num ,' is: ', accumulator

end program factorial

