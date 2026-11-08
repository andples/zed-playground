(* Inlay hints show the inferred types of [area] and [describe]. *)

type shape = Circle of float | Rect of float * float

let area = function
  | Circle r -> Float.pi *. r *. r
  | Rect (w, h) -> w *. h

let describe s =
  match s with
  | Circle r -> Printf.sprintf "circle r=%g, area %.2f" r (area s)
  | Rect (w, h) -> Printf.sprintf "rect %gx%g, area %.2f" w h (area s)
