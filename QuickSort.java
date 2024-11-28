public class QuickSort {
    static int ctr = 0;

    static int partition(Object[] arr, int lb, int ub) {

        int pivot = Integer.parseInt((arr[lb].toString().split(","))[3]);
        Object pivotObject = arr[lb];
        int down = lb;
        int up = ub;
        while (down < up) {
            while (down <= ub &&

                    Integer.parseInt((arr[down].toString().split(","))[3]) <= pivot) {

                down++;
            }
            while (Integer.parseInt((arr[up].toString().split(","))[3]) >

                    pivot) {

                up--;
            }
            if (down < up) {
                Object temp = arr[up];
                arr[up] = arr[down];
                arr[down] = temp;
            }
        }
        arr[lb] = arr[up];
        arr[up] = pivotObject;
        return up;
    }

    static void quick(Object[] arr, int lb, int ub) {
        ctr++;
        if (lb >= ub)
            return;
        int mid = partition(arr, lb, ub);
        quick(arr, lb, mid - 1);
        quick(arr, mid + 1, ub);
    }

    static Object[] start(Object[] arr, int lb, int ub) {
        quick(arr, lb, ub);
        return arr;
    }
}