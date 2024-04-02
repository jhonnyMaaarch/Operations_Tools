program fortran_maths
   implicit none
   
   integer :: single_num
   real :: dbl_num
   complex :: fl_number
   character :: letter
   logical :: isOkay

   print *, 'What is the single number: '
   read(*,*) single_num
   
   print *, 'What is the double number: '
   read(*,*) dbl_num
   
   print *, 'What is the floating point number: '
   read(*,*) fl_number

   print *, 'What is the single letter: '
   read(*,*) letter

   print *, 'Is it okay or not: '
   read(*,*) isOkay

   print *, 'The single number is ', single_num
   
   print *, 'The double number is ', dbl_num
   
   print *, 'The floating number is ', fl_number
   
   print *, 'The single letter is ', letter
   
   print *, 'it is ', isOkay

end program fortran_maths
