program rectangle
   implicit none
   
   real :: length
   real :: width
   real :: Area
   real :: perimeter

   print *, 'Enter the length: '
   read (*,*) length
   print *, 'Enter the width: '
   read (*,*) width
   
   Area = length * width
   perimeter = 2 * Area

   print *, 'The Area of the rectangle is (Area): ',  Area
   print *, 'The perimeter of the rectangle is (perimeter): ',  perimeter

end program rectangle
