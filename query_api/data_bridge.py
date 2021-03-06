# Module to bridge API with ORM
import json
import os
import pprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://cantor:navigational@localhost/postgres')
Session = sessionmaker(bind=engine)
session = Session()

# DB Utils

def selection_query(text):
    """
    Runs a selection query on the database
    Post-processes the data into valid GeoJSON
    This is dependent on the Schema of the table...maybe?
    """
    result = session.execute(text)
    header = result.keys()
    print(header)
    row = result.fetchone()
    feature_collection = {"type":"FeatureCollection"}
    feature_collection["features"] = []
    while row is not None:
        print("Row: ", row)
        feature = {"type":"Feature"}
        if row[0]:
            feature["geometry"] = json.loads(row[0])
            if row[1] is not None:
                feature["properties"] = {}
                feature["properties"]["name"] = row[1]
                feature["properties"]["marker-symbol"] = "marker"
                for col, r in zip(header[1:] ,row[1:]):
                    feature["properties"][col] = r
                feature_collection["features"].append(feature)
        row = result.fetchone()
    #pprint.pprint(feature_collection)
    return feature_collection


def text_query(text):
    fc = selection_query(text)
    return fc
    #return json.dumps(fc, sort_keys=True)

def load_json_from_file(filename):
    with open('query_api/ex1.geojson', 'r') as geofile:
        ex_geojson = json.load(geofile)
    return ex_geojson
    


def test_query(text):
    result = session.execute(text);
    session.commit()
    return {"Test":result.keys()[0]}

