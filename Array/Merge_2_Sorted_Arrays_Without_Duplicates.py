nums1=[1,1,2,2,3,4,5]
nums2=[1,2,3,3,5,6]
def merge_sorted_array(nums1,nums2):
    i=0
    j=0
    result=[]
    n=len(nums1)
    m=len(nums2)
    while i<n and j<m:
        if nums1[i]<nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1 
        elif nums2[j]<nums1[i]:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1
        else:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
            j+=1
    while i<n:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
            
    while j<m:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1
    return result

print(merge_sorted_array(nums1,nums2))

