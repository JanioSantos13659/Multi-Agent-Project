import time


class ResourceAgent:
    def provide(self, resource):
        print(f"[Resource] Providing: {resource}")
        time.sleep(1)
        return f"Resource '{resource}' delivered"

    # Backward compatibility with existing Portuguese method calls.
    def fornecer(self, recurso):
        return self.provide(recurso)


# Backward compatibility with existing Portuguese class imports.
AgenteRecurso = ResourceAgent
