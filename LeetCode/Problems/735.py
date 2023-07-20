# Daily challenge in 2023.07.20
# 735. Asteroid Collision
# Difficulty : Medium
# Algorithm : Stack
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 116 ms (38.27%), Memory : 17.60 MB (57.73%)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Time compleixty : O(N), Space complexity : O(N)
        stack = []

        for ast in asteroids:
            if not stack:
                stack.append(ast)
                continue

            while stack:
                now = stack.pop()

                # two asteroids meet
                if now > 0 and ast < 0:

                    # the smaller one will explode
                    if abs(now) > abs(ast):
                        stack.append(now)
                        break
                    elif abs(now) < abs(ast):
                        if not stack:
                            stack.append(ast)
                            break
                        continue
                    # if both are the same size, both will explode
                    else:
                        break

                # never meet
                else:
                    stack.append(now)
                    stack.append(ast)
                    break

        return stack
