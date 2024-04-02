program arithmetic
   implicit none

   integer :: first_num
   integer :: sec_num
   character :: task
   !logical :: operation_type
   integer :: answer

   print *, 'Enter first number: '
   read(*,*) first_num
   print *, 'Enter second number: '
   read(*,*) sec_num
   print *, 'Enter the operation you will like to be performed (+, -, /, *, **): '
   read(*,*) task
  
   select case (task)
     case ('+') 
          answer = first_num + sec_num
     case ('-')
          answer = first_num - sec_num
     case ('/')
          answer = first_num / sec_num
     case ('*')
          answer = first_num * sec_num
     case ('**')
          answer = first_num ** sec_num
     case default
          print *, 'Invalid Operation!'
          stop
     end select
          
   print *, 'The result of your operation is (answer): ', answer


end program arithmetic
