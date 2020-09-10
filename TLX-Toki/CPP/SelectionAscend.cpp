void selection_asc()
{
    int i,temp,j,imax;
    for (i=0;i<n-1;i++){
		imax =i;
        for (j=i+1;j<n;j++){
			if (A[j] < A[imax]) imax = j;
		}
        temp  = A[i];
        A[i]  = A[imax];
        A[imax]= temp;
    }
}