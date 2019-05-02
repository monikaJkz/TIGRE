import numpy as np
import tigre
import os

niter = 20
dirname = os.path.dirname(__file__)
keywords = dict(blocksize=20)


def save_config(dict, name):
    for kw in dict:
        if kw not in ['nproj', 'geo', 'angles', 'niter', 'kwargs']:
            raise KeyError()
    np.save(os.path.join(dirname, name),dict)


if __name__ == '__main__':
    save_config(dict(
        nproj=100,
        niter = 20,
        geo=tigre.geometry(mode='cone', default=True, high_quality=True),
        angles=np.linspace(0, 2 * np.pi, 100),
        kwargs=keywords
    ),
        'configuration1.npy')

    save_config(dict(
        nproj=100,
        niter = 20,
        geo=tigre.geometry(mode='parallel', default=True, high_quality=True),
        angles=np.linspace(0, 2 * np.pi, 100),
        kwargs=keywords
    ),
        'configuration2.npy')

    save_config(dict(
        nproj=100,
        niter=20,
        geo=tigre.geometry(mode='cone', default=True,
                           nVoxel=np.array([480,480,512])),
        angles=np.linspace(0, 2 * np.pi, 100),
        kwargs=keywords
    ),
        'configuration3.npy')

    save_config(dict(
        nproj=100,
        niter=20,
        geo=tigre.geometry(mode='parallel', default=True,
                           nVoxel=np.array([480, 480, 512])),
        angles=np.linspace(0, 2 * np.pi, 100),
        kwargs=keywords
    ),
        'configuration4.npy')