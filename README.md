# python-handy
## python serve path
```bash
python -m http.server
```
## leading zeros
```python
>f"{329:05d}"
00329
```
## websocket client
```bash
python -m websockets <uri>
```
## PyYaml
```python
import yaml

data = yaml.load(fp,yaml.SafeLoader)
yaml.dump(data,new_fp,yaml.SafeLoader)
```
