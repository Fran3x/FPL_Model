import streamlit as st
import pandas as pd
import os
import time
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

def page3():
    st.title("Model architecture")

    with Diagram("Web Service", show=False):
        ELB("lb") >> EC2("web") >> RDS("userdb")