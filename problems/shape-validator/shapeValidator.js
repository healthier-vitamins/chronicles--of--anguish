let lastPoint = null;

// Example usage
const existingLines = [];

// Utility function to determine the determineOrientation of three points
function determineOrientation(firstPoint, secondPoint, thirdPoint) {
  const val =
    (secondPoint.y - firstPoint.y) * (thirdPoint.x - secondPoint.x) -
    (secondPoint.x - firstPoint.x) * (thirdPoint.y - secondPoint.y);

  if (val === 0) return 0;
  return val > 0 ? 1 : 2;
}

// // Utility function to determine the orientation of three points
// function determineOrientation(firstPoint, secondPoint, thirdPoint) {
//   const val =
//     (secondPoint.y - firstPoint.y) * (thirdPoint.x - secondPoint.x) -
//     (secondPoint.x - firstPoint.x) * (thirdPoint.y - secondPoint.y);

//   if (val === 0) return 0;
//   return val > 0 ? 1 : 2;
// }

// Utility function to check if two line segments intersect, excluding endpoints
function doIntersect(
  existingFirstPoint,
  existingSecondPoint,
  newFirstPoint,
  newSecondPoint
) {
  const o1 = determineOrientation(
    existingFirstPoint,
    existingSecondPoint,
    newFirstPoint
  );
  const o2 = determineOrientation(
    existingFirstPoint,
    existingSecondPoint,
    newSecondPoint
  );
  const o3 = determineOrientation(
    newFirstPoint,
    newSecondPoint,
    existingFirstPoint
  );
  const o4 = determineOrientation(
    newFirstPoint,
    newSecondPoint,
    existingSecondPoint
  );
  console.log("o1, ", o1);
  console.log("o2, ", o2);
  console.log("o3, ", o3);
  console.log("o4, ", o4);
  // General case
  if (o1 !== o2 && o3 !== o4) {
    return true;
  }

  const allPoints = [
    existingFirstPoint,
    existingSecondPoint,
    newFirstPoint,
    newSecondPoint,
  ];

  // Special cases, excluding intersections at the endpoints
  if (
    withinRange(existingFirstPoint, newFirstPoint, existingSecondPoint) &&
    withinRange(existingFirstPoint, existingSecondPoint, newFirstPoint)
  )
    return true;
  if (
    withinRange(existingFirstPoint, newSecondPoint, existingSecondPoint) &&
    withinRange(existingFirstPoint, existingSecondPoint, newSecondPoint)
  )
    return true;
  if (
    withinRange(newFirstPoint, existingFirstPoint, newSecondPoint) &&
    withinRange(newFirstPoint, newSecondPoint, existingFirstPoint)
  )
    return true;
  if (
    withinRange(newFirstPoint, existingSecondPoint, newSecondPoint) &&
    withinRange(newFirstPoint, newSecondPoint, existingSecondPoint)
  )
    return true;

  return false;
}

// Function to add a new point and check if it forms a line segment that intersects with existing line segments
function addPoint(existingLines, newPoint) {
  // for first point only
  if (lastPoint === null) {
    lastPoint = newPoint;
    return true;
  }

  const newLine = [lastPoint, newPoint];

  for (let i = 0; i < existingLines.length; i++) {
    const line = existingLines[i];
    console.log("line, ", line);
    console.log("new line, ", newLine);

    if (doIntersect(line[0], line[1], newLine[0], newLine[1])) {
      return false;
    }
  }

  existingLines.push(newLine);
  lastPoint = newPoint;
  return true;
}

// const point1 = { x: 0, y: 0 };
// const point2 = { x: 5, y: 5 };
// const point3 = { x: 1, y: 1 };
// const point4 = { x: 6, y: 6 };

const point1 = { x: 1, y: 1 };
const point2 = { x: 5, y: 1 };
const point3 = { x: 5, y: 5 };
const point4 = { x: 4, y: 0 };

// const point1 = { x: 1, y: 1 };
// const point2 = { x: 5, y: 1 };
// const point3 = { x: 5, y: 5 };
// const point4 = { x: 3, y: 5 };
// const point5 = { x: 5, y: 0 };

console.log(addPoint(existingLines, point1)); // true
console.log(addPoint(existingLines, point2)); // true
console.log(addPoint(existingLines, point3)); // true
console.log(addPoint(existingLines, point4)); // false

// function doLinesIntersect(line1, line2) {
//   function ccw(A, B, C) {
//     return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x);
//   }

//   const [A, B] = line1;
//   const [C, D] = line2;

//   return ccw(A, C, D) !== ccw(B, C, D) && ccw(A, B, C) !== ccw(A, B, D);
// }

// function canAddLine(existingLines, newLine) {
//   for (let i = 0; i < existingLines.length; i++) {
//     if (doLinesIntersect(existingLines[i], newLine)) {
//       return false;
//     }
//   }
//   return true;
// }

// let existingLines = [
//   // Add pre-existing lines as arrays of two points.
//   // Each point is an object with 'x' and 'y' properties.
//   // Example:
//   // [{x: 0, y: 0}, {x: 1, y: 1}],
//   // [{x: 2, y: 2}, {x: 3, y: 3}]
// ];

// function addLine(x1, y1, x2, y2) {
//   const newLine = [
//     { x: x1, y: y1 },
//     { x: x2, y: y2 },
//   ];

//   if (canAddLine(existingLines, newLine)) {
//     existingLines.push(newLine);
//     return true;
//   } else {
//     return false;
//   }
// }

// // Example usage
// console.log(addLine(0, 0, 1, 1)); // true (no intersection)
// console.log(addLine(2, 2, 3, 3)); // true (no intersection)
// console.log(addLine(0, 0, 3, 3)); // false (intersection)
