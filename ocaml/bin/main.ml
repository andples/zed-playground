let () =
  [ Shapes.Circle 1.0; Shapes.Rect (2.0, 3.0) ]
  |> List.iter (fun s -> print_endline (Shapes.describe s))
