import numpy as np
import cv2 as cv


class ImageProcessor:

    net = None
    ln = None
    classes: dict[int | str, int | str] = {}
    colors = []

    def __init__(
        self,
        objDir: str,
        img_size: tuple[int, int],
        cfg_file: str,
        weights_file: str,
        result_path: str,
    ):
        np.random.seed(42)
        self.net = cv.dnn.readNetFromDarknet(cfg_file, weights_file)
        self.net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
        self.ln = self.net.getLayerNames()
        self.ln = [self.ln[i - 1] for i in self.net.getUnconnectedOutLayers()]
        self.width: int = img_size[0]
        self.height: int = img_size[1]
        self.result_path = result_path

        with open(f"{objDir}\\obj.names", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            self.classes[i] = line.strip()

        # If you plan to utilize more than six classes, please include additional colors in this list.
        self.colors = [
            (0, 0, 255),
            (0, 255, 0),
            (255, 0, 0),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255),
            (0, 0, 125),
            (0, 125, 0),
            (125, 0, 0),
            (125, 125, 125),
            (125, 0, 125),
            (0, 125, 125),
            (0, 0, 255),
            (0, 255, 0),
            (255, 0, 0),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255),
            (0, 0, 125),
            (0, 125, 0),
            (125, 0, 0),
            (125, 125, 125),
            (125, 0, 125),
            (0, 125, 125),
        ]

    def proccess_image(self, img, name):  # type: ignore

        blob = cv.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)  # type: ignore
        self.net.setInput(blob)  # type: ignore
        outputs: np.uint8 = self.net.forward(self.ln)  # type: ignore
        outputs = np.vstack(outputs)  # type: ignore

        coordinates: dict[int | str, int | str] = self.get_coordinates(outputs, 0.2)  # type: ignore
        if self.draw_identified_objects(img, coordinates, name):  # type: ignore
            return coordinates
        return 0

    def get_coordinates(self, outputs, conf) -> dict[int | str, int | str]:  # type: ignore

        boxes = []
        confidences = []
        classIDs = []

        for output in outputs:  # type: ignore
            scores = output[5:]  # type: ignore

            classID = np.argmax(scores)  # type: ignore
            confidence = scores[classID]  # type: ignore
            if confidence > conf:
                x, y, w, h = output[:4] * np.array(  # type: ignore
                    [self.width, self.height, self.width, self.height]
                )
                p0 = int(x - w // 2), int(y - h // 2)  # type: ignore
                boxes.append([*p0, int(w), int(h)])  # type: ignore
                confidences.append(float(confidence))  # type: ignore
                classIDs.append(classID)  # type: ignore

        indices = cv.dnn.NMSBoxes(boxes, confidences, conf, conf - 0.1)  # type: ignore

        if len(indices) == 0:
            return []  # type: ignore

        coordinates = []
        for i in indices.flatten():  # type: ignore
            (x, y) = (boxes[i][0], boxes[i][1])  # type: ignore
            (w, h) = (boxes[i][2], boxes[i][3])  # type: ignore

            coordinates.append(  # type: ignore
                {
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                    "class": classIDs[i],
                    "class_name": self.classes[classIDs[i]],
                }
            )
        return coordinates  # type: ignore

    def draw_identified_objects(self, img, coordinates, name) -> None:  # type: ignore
        for coordinate in coordinates:  # type: ignore
            x = coordinate["x"]  # type: ignore
            y = coordinate["y"]  # type: ignore
            w = coordinate["w"]  # type: ignore
            h = coordinate["h"]  # type: ignore
            classID = coordinate["class"]  # type: ignore

            color = self.colors[classID]  # type: ignore

            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)  # type: ignore
            cv.putText(  # type: ignore
                img,
                self.classes[classID],  # type: ignore
                (x, y - 10),
                cv.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2,
            )

            return cv.imwrite(f"{self.result_path}\\{name}", img)  # type: ignore

        # cv.imshow("window", img)


# while True:


#     # ss = np.array(ImageGrab.grab())  # BGR Image
#     # ss = cv.cvtColor(ss, cv.COLOR_RGB2BGR)

#     if cv.waitKey(1) == ord("q"):
#         cv.destroyAllWindows()
#         break

#     # coordinates = processor.proccess_image(ss)
#     # for c in coordinates:
#     #     print(c["class_name"])

#     # # If you have limited computer resources, consider adding a sleep delay between detections.
#     # sleep(1)

# print("Finished.")
