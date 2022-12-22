# pycatia-drawing-template

This script tries to be a feature rich example of how to create a drawing border
within CATIA V5 template using pycatia.

It'll never be a one-stop solution for everyone but should help overcome many
hurdles for those new to scripting with pycatia within the drafting workbench.


## Requirements
* Windows 
* CATIA V5 - 
* python >= 3.9
* pycatia >= 0.5.7 - https://github.com/evereux/pycatia
  * You can either install pycatia within your own python development 
  environment or grab the pre-built binary available on the releases page.

## Usage
### Python & Git
* Install python.
* Clone this repository using git. git clone https://github.com/evereux/pycatia-drawing-template.git
* Change directory into the newly created repository folder.
* Create and activate a virtual environment.
* Install the requirements
  * pip install -r requirements
* Run the script.
  * python main.py -draw-existing
    * This option requires a new empty CATDrawing document to already be open.