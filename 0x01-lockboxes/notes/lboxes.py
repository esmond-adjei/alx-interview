visited_boxes = [0]

def check_boxes(boxes):
    if boxes[box[key]] in visited_boxes:
        return
    else:
        visited_boxes.append(boxes[box[key]])
    check_boxes(boxes[box])
