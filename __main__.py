# -*- coding: utf-8 -*-

from logging import getLogger, DEBUG
import os
import glob

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import cognitive_face as CF

# Replace with a valid subscription key (keeping the quotes in place).
KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
CF.Key.set(KEY)

CF.BaseUrl.set('https://xxxxxxxxxxxx.api.cognitive.microsoft.com/face/v1.0')

def list_person_group():
    person_groups = CF.person_group.lists()
    return person_groups

def get_person_group(person_group_id):
    CF.person_group.get(person_group_id)

def delete_person_group(person_group_id):
    CF.person_group.delete(person_group_id)
    return

def create_person_group(person_group_id):
    CF.person_group.create(person_group_id)
    person_group = CF.person_group.get(person_group_id)
    return person_group

def list_persons(person_group_id,):
    person_ids = CF.person.lists(person_group_id)
    return person_ids

def delete_person(person_group_id, person_id):
    CF.person.delete(person_group_id, person_id)
    return

def get_person(person_group_id, person_id):
    person = CF.person.get(person_group_id, person_id)
    return person

def create_person(person_group_id, person_name):
    person_id = CF.person.create(person_group_id, person_name)
    return person_id

def add_face(image, person_group_id, person_id):
    persisted_face_id = CF.person.add_face(image, person_group_id, person_id)
    return persisted_face_id

def get_face(person_group_id, person_id, persisted_face_id):
    persisted_face = CF.person.get_face(person_group_id, person_id, persisted_face_id)
    return persisted_face

def delete_face(person_group_id, person_id, persisted_face_id):
    CF.person.delete_face(person_group_id, person_id, persisted_face_id)

def get_person_id(person_group_id, person_name):
    persons = CF.person.lists(person_group_id)
    for person in persons:
        # logger.info(person)
        if person['name'] == person_name:
            return person['personId']
    return None

def get_person_name(person_group_id, person_id):
    persons = CF.person.lists(person_group_id)
    for person in persons:
        # logger.info(person)
        if person['personId'] == person_id:
            return person['name']
    return None

def train(person_group_id):
    CF.person_group.train(person_group_id)

def get_train_status(person_group_id):
    train_status = CF.person_group.get_status(person_group_id)
    return train_status

def face_detection(image):
    faces = CF.face.detect(image)
    return faces

def identify(face_id, person_group_id):
    persons = CF.face.identify(face_id, person_group_id)
    return persons

def main():
    logger.debug("start main")
    # person_name = 'username'
    # person_group_id = 'my-person-group'

    # List PersonGroup
    # person_groups = list_person_group()
    # logger.info(person_groups)

    # Create PersonGroup
    # person_group = create_person_group(person_group_id)
    # logger.info(person_group)

    # Create Person
    # person_id = create_person(person_group_id, person_name)
    # logger.info(person_id)

    # Get Person ID
    # person_id = get_person_id(person_group_id, person_name)
    # logger.info(person_id)


    # Add Person Face
    # image_paths = glob.glob(os.getcwd()+'/images/'+person_name+'/*.jpg')
    # for image_path in image_paths:
    #     # logger.info(image_path)
    #     image = open(image_path)
    #     persisted_face_id = add_face(image, person_group_id, person_id)
    #     logger.info(persisted_face_id)
    #     image.close()

    # Delete Person Face
    # person = get_person(person_group_id, person_id)
    # for persisted_face_id in person['persistedFaceIds']:
    #     delete_face(person_group_id, person_id, persisted_face_id)

    # Train
    # train(person_group_id)

    # Get Train Status
    # train_status = get_train_status(person_group_id)
    # logger.info(train_status)

    # Detect
    # image = open('images/'+person_name+'.jpg')
    # faces = face_detection(image)
    # image.close()
    # face_ids = []
    # for face in faces:
    #     face_ids.append(face['faceId'])
    
    # Identify
    # persons = identify(face_ids, person_group_id)
    # logger.info(persons)

    # for person in persons:
    #     logger.info(person)
    #     for i, candidate in enumerate(person['candidates']):
    #         logger.info(candidate)
    #         if i == 0:
    #             candidate_name = get_person_name(person_group_id, candidate['personId'])
    #             confidence = str(candidate['confidence'])
    #             logger.info('candidate: '+candidate_name)
    #             logger.info('confidence: '+confidence)

if __name__ == "__main__":
    main()