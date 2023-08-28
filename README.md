# Hough Transform (Line and Circle Detection)
The Hough transform is a method that, in theory, can be used to find features of any shape in an image. In practice it is only generally used for finding straight lines or circles. 

# Line Detection with Hough Transform
Let (x, y) be a coordinate in an image and (m, b) be a coordinate in Hough space. We can observe that a line (defined by m₀ and b₀) in the image space ( where axis is x and y) corresponds to a point in Hough space (where axis is m and b), and Vice Versa (point in image space corresponds to a line in Hough space). More specifically, Hough Transform finds all possible lines which pass a point (x₀, y₀), and each line can be parametrized by a point (m₀, b₀) in Hough space. Therefore, the collection of all (m₀, b₀) becomes a line in Hough space.

![image](https://github.com/bakhshiintel/hough/assets/98385786/d8ceb6bd-b62f-4637-b8bd-6def23f00dba)



# Circle Detection with Hough Transform
Similar to line detection, this time we define a Hough space for circle which is parameterized by (a, b, r), where the center is (a,b) and radius is r.

If r is known, then Hough space is two-dimensional and works almost in a same way as line detection. Hough transform of Circle draws, in Hough space, all possible locations of circle center for each edge point (x, y) in image space. The set of all possible circle centers, which is a Hough Transform output, given an edge point (x, y) with fixed radius r is again a circle in Hough space as is illustrated below. Then the circle center, what we are looking for, in image space is determined by parameter (a, b) at which the accumulator array H[a,b] gets the most votes.

![image](https://github.com/bakhshiintel/hough/assets/98385786/cd60d80e-8348-4ce1-a9d0-e3eef12376b6)
