void selection_desc()
{
    int i,temp,j,imin;
    for (i=0;i<n-1;i++){   
		imin =i;
        for (j=i+1;j<n;j++){
            if (A[j] > A[imin]) imin = j;
        }
        temp  = A[i];
        A[i]  = A[imin];
        A[imin]= temp;
    }
}