(* Standard ML is a blazingly standardized hit functional programming language 
   
  use any compiler/interpreter you would like (SML/NJ, MLTon, LunarML, MLKit, MOSML, AliceML, ...)
  feed the standard output to a file OR the stdin of a compiler/interpreter

  accepts a positional argument via commandline input 
*)
  

val (rawn :: _) = CommandLine.arguments () handle _ => raise Fail "expected a positional argument, found none"
val n = Option.valOf (Int.fromString rawn) handle _ => raise Fail "argument was not a valid integer"
val _ = print (String.concat 
      (["val n = ", Int.toString n, "\n", "val _ = ((fn x => print (x ^ \"\\n\")) o Bool.toString) (\n"] @
        List.tabulate(n + 1, (fn x => "if n = " ^ Int.toString x ^ " then " ^ Bool.toString (x mod 2 = 0) ^ " else \n")) @ 
       ["raise Fail \"Unreachable\")"]))


