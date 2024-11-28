#include <stdio.h>

#define MAX 1000
#define INF 1000000007

int main() {
    int i, j, k, l, res;
    int dim[6] = {5, 10, 4, 6, 10, 2};
    int dp[MAX][MAX] = {0};

    for (i = 0; i < 5; i++) {
        dp[i][i] = 0;
    }

    for (l = 2; l <= 5; l++) {
        for (i = 0; i <= 5 - l; i++) {
            j = i + l - 1;
            dp[i][j] = INF;
            for (k = i; k < j; k++) {
                res = dp[i][k] + dp[k + 1][j] + (dim[i] * dim[k + 1] * dim[j + 1]);
                if (res < dp[i][j]) {
                    dp[i][j] = res;
                }
            }
        }
    }

    printf("Minimum cost: %d\n", dp[0][4]);

    printf("Cost table:\n");
    for (i = 0; i < 5; i++) {
        for (j = i; j < 5; j++) {
            printf("Cost[%d][%d] = %d\n", i, j, dp[i][j]);
        }
    }

    return 0;
}
