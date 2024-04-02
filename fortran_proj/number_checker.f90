program even_odd
   implicit none
   
   integer :: given_num, reg_num, remainder
   
   reg_num = 2
   !remainder = mod(given_num, reg_num)
   

   print*,'Enter a number (given_num): '
   read(*,*) given_num

   remainder = mod(given_num, reg_num)   

   if (remainder == 0) then
      print*,'The given number is even!'
   else
      print*,'The given number is odd!'
   end if

end program even_odd
 

   
