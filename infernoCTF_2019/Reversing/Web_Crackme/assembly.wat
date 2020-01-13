(module


  (memory 1)


  (func $myFunction1 (result i32)

   (i32.store
      (i32.const 0)
      (i32.const 0xd359beef) 

    )

    (i32.store
      (i32.const 3)
      (i32.const 0x5579) 

    )
	
	(i32.store
	(i32.const 5)
	(i32.const 0x66) 

	)


    (i32.load
      (i32.const 2)
    )
  )
  
  
  (func $myFunction2 (result i32)
    (i32.store
      (i32.const 0)
      (i32.const 0xc939ba2d) 

    )

   (i32.store
      (i32.const 3)
      (i32.const 0x7165) 

    )
	
	(i32.store16
	(i32.const 4)
	(i32.const 0x2D4D) 

	)

    (i32.load
      (i32.const 2)
    )
  )
  
  

  (export "myFunction1" (func $myFunction1))
  (export "myFunction2" (func $myFunction2))

)