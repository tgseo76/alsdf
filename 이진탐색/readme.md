```python
def search(st,en,tg):

if st==en:
//
return


mid =(st+en)//2

if nums[mid]<target:
    search(mid+1,en,tg)
else:
    search(st,mid,target)
```
