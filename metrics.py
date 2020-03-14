import skimage.metrics

# Configuration for metrics to calculate
metrics = [
    {
        "name": 'Mean-Squared Error',
        "apply": lambda original, filtered: skimage.metrics.mean_squared_error(original, filtered)
    },
    {
        "name": 'Normalized Root Mean-Squared Error',
        "apply": lambda original, filtered: skimage.metrics.normalized_root_mse(original, filtered)
    },
    {
        "name": 'Peak Signal to Noise Ratio',
        "apply": lambda original, filtered: skimage.metrics.peak_signal_noise_ratio(original, filtered)
    }
]
