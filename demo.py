# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
from PIL import Image
import os
from time import clock
os.environ['DISPLAY'] = '0.0'


from utils import load_coco_names, draw_boxes, get_boxes_and_inputs, get_boxes_and_inputs_pb, non_max_suppression, \
                  load_graph, letter_box_image

FLAGS = tf.app.flags.FLAGS

#tf.app.flags.DEFINE_string('input_img', '', 'Input image')
tf.app.flags.DEFINE_string('input_img', './PID000.jpg', 'Input image')

#tf.app.flags.DEFINE_string('output_img', '', 'Output image')
tf.app.flags.DEFINE_string('output_img', './pPID000.jpg', 'Output image')
tf.app.flags.DEFINE_string('class_names', './obj.names', 'File with class names')
tf.app.flags.DEFINE_string('weights_file', './my-yolov3_last.weights', 'Binary file with detector weights')
tf.app.flags.DEFINE_string('data_format', 'NCHW', 'Data format: NCHW (gpu only) / NHWC')
tf.app.flags.DEFINE_string('ckpt_file', './saved_model/model.ckpt', 'Checkpoint file')
tf.app.flags.DEFINE_string('frozen_model', './frozen_darknet_yolov3_model.pb', 'Frozen tensorflow protobuf model')
tf.app.flags.DEFINE_bool('tiny', False, 'Use tiny version of YOLOv3')
tf.app.flags.DEFINE_integer('size', 416, 'Image size')

tf.app.flags.DEFINE_float('conf_threshold', 0.4, 'Confidence threshold')
tf.app.flags.DEFINE_float('iou_threshold', 0.4, 'IoU threshold')
tf.app.flags.DEFINE_float('gpu_memory_fraction', 1.0, 'Gpu memory fraction to use')

def main(input_path, DEBUG):
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=FLAGS.gpu_memory_fraction)
    config = tf.ConfigProto(
        gpu_options=gpu_options,
        log_device_placement=False,
    )
    classes = load_coco_names(FLAGS.class_names)
    frozenGraph = load_graph(FLAGS.frozen_model)
    boxes, inputs = get_boxes_and_inputs_pb(frozenGraph)
    boxes_list = []
    with tf.Session(graph=frozenGraph, config=config) as sess:
        for item in input_path:
            start = clock()
            FLAGS.input_img = item
            img = Image.open(FLAGS.input_img)
            img_resized = letter_box_image(img, FLAGS.size, FLAGS.size, 128)
            img_resized = img_resized.astype(np.float32)
            detected_boxes = sess.run(boxes, feed_dict={inputs: [img_resized]})
            filtered_boxes = non_max_suppression(detected_boxes, confidence_threshold=FLAGS.conf_threshold,iou_threshold=FLAGS.iou_threshold)
            boxes_list.append(filtered_boxes)
            if DEBUG:
                draw_boxes(filtered_boxes, img, classes, (FLAGS.size, FLAGS.size), True)
            print(filtered_boxes)
            print("Execution Time : {} / #Symbols : {}  / Path : {}".format(clock()-start, len(filtered_boxes), item))
        sess.close()
    tf.reset_default_graph()
    return boxes_list, classes, FLAGS.size


