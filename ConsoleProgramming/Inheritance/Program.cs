Console.WriteLine("Enter Length:");
int length = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Enter Width:");
int width = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Enter Height:");
int height = Convert.ToInt32(Console.ReadLine());

var cube = new Cube(width, height, length);

var triangle = new Triangle();
var triangle2 = new Triangle() { Height = height, Length = length, Hypotenuese = 10 };
var triangle1 = new Triangle(10);
var triangle3 = new Triangle(10, height, length);

var rectangle = new Rectangle() { Length = length, Width = width };

Console.WriteLine("Cube Area Is: " + cube.getArea());
Console.WriteLine("Cube Volume Is: " + cube.getVolume());

Console.WriteLine("Triangle Area Is: " + triangle.getArea());
Console.WriteLine("Triangle2 Area Is: " + triangle2.getArea());
Console.WriteLine("Triangle1 Area Is: " + triangle1.getArea());
Console.WriteLine("Triangle3 Area Is: " + triangle3.getArea());

Console.WriteLine("Rectangle Area Is: " + rectangle.getArea());
