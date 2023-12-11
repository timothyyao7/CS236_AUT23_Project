from nerfbusters.nerf.experiment_configs.utils import Argument

arguments_list_of_lists = []

output_folder = "outputs-postprocessed"

dataset_lists = [
    # Argument(
    #     name="aloe",
    #     arg_string=f"--data data/nerfbusters-dataset/aloe --pipeline.nerf_checkpoint_path outputs-checkpoints/aloe-baseline.ckpt --output-dir {output_folder}/aloe",
    # ),
    # Argument(
    #     name="art",
    #     arg_string=f"--data data/nerfbusters-dataset/art --pipeline.nerf_checkpoint_path outputs-checkpoints/art-baseline.ckpt --output-dir {output_folder}/art",
    # ),
    # Argument(
    #     name="car",
    #     arg_string=f"--data data/nerfbusters-dataset/car --pipeline.nerf_checkpoint_path outputs-checkpoints/car-baseline.ckpt --output-dir {output_folder}/car",
    # ),
    # Argument(
    #     name="century",
    #     arg_string=f"--data data/nerfbusters-dataset/century --pipeline.nerf_checkpoint_path outputs-checkpoints/century-baseline.ckpt --output-dir {output_folder}/century",
    # ),
    # Argument(
    #     name="flowers",
    #     arg_string=f"--data data/nerfbusters-dataset/flowers --pipeline.nerf_checkpoint_path outputs-checkpoints/flowers-baseline.ckpt --output-dir {output_folder}/flowers",
    # ),
    # Argument(
    #     name="garbage",
    #     arg_string=f"--data data/nerfbusters-dataset/garbage --pipeline.nerf_checkpoint_path outputs-checkpoints/garbage-baseline.ckpt --output-dir {output_folder}/garbage",
    # ),
    # Argument(
    #     name="picnic",
    #     arg_string=f"--data data/nerfbusters-dataset/picnic --pipeline.nerf_checkpoint_path outputs-checkpoints/picnic-baseline.ckpt --output-dir {output_folder}/picnic",
    # ),
    # Argument(
    #     name="pikachu",
    #     arg_string=f"--data data/nerfbusters-dataset/pikachu --pipeline.nerf_checkpoint_path outputs-checkpoints/pikachu-baseline.ckpt --output-dir {output_folder}/pikachu",
    # ),
    # Argument(
    #     name="pipe",
    #     arg_string=f"--data data/nerfbusters-dataset/pipe --pipeline.nerf_checkpoint_path outputs-checkpoints/pipe-baseline.ckpt --output-dir {output_folder}/pipe",
    # ),
    # Argument(
    #     name="plant",
    #     arg_string=f"--data data/nerfbusters-dataset/plant --pipeline.nerf_checkpoint_path outputs-checkpoints/plant-baseline.ckpt --output-dir {output_folder}/plant",
    # ),
    # Argument(
    #     name="roses",
    #     arg_string=f"--data data/nerfbusters-dataset/roses --pipeline.nerf_checkpoint_path outputs-checkpoints/roses-baseline.ckpt --output-dir {output_folder}/roses",
    # ),
    # Argument(
    #     name="table",
    #     arg_string=f"--data data/nerfbusters-dataset/table --pipeline.nerf_checkpoint_path outputs-checkpoints/table-baseline.ckpt --output-dir {output_folder}/table",
    # ),
    # Argument(
    #     name="poster",
    #     arg_string=f"--data data/nerfbusters-dataset/poster --pipeline.nerf_checkpoint_path outputs-checkpoints/poster-baseline.ckpt --output-dir {output_folder}/poster"
    # ),
    # Argument(
    #     name="hoover",
    #     arg_string=f"--data data/stanford-dataset/hoover --pipeline.nerf_checkpoint_path outputs-checkpoints/hoover-baseline.ckpt --output-dir {output_folder}/hoover"
    # ),
    # Argument(
    #     name="hoover-night",
    #     arg_string=f"--data data/stanford-dataset/hoover-night --pipeline.nerf_checkpoint_path outputs-checkpoints/hoover-night-baseline.ckpt --output-dir {output_folder}/hoover-night"
    # ),
    # Argument(
    #     name="hoover-night-b",
    #     arg_string=f"--data data/stanford-dataset/hoover-night-b --pipeline.nerf_checkpoint_path outputs-checkpoints/hoover-night-b-baseline.ckpt --output-dir {output_folder}/hoover-night-b"
    # ),
    # Argument(
    #     name="hoover-dawn",
    #     arg_string=f"--data data/stanford-dataset/hoover-dawn --pipeline.nerf_checkpoint_path outputs-checkpoints/hoover-dawn-baseline.ckpt --output-dir {output_folder}/hoover-dawn"
    # ),
    Argument(
        name="hoover-mix",
        arg_string=f"--data data/stanford-dataset/hoover-mix --pipeline.nerf_checkpoint_path outputs-checkpoints/hoover-mix-baseline.ckpt --output-dir {output_folder}/hoover-mix"
    )
]
arguments_list_of_lists.append(dataset_lists)

experiments_list = [
    Argument(
        name="nerfacto",
        arg_string="--pipeline.use_visibility_loss False --pipeline.use_singlestep_cube_loss False",
    ),
    Argument(
        name="nerfacto-visibility",
        arg_string="--pipeline.use_visibility_loss True --pipeline.use_singlestep_cube_loss False",
    ),
    Argument(
        name="nerfacto-visibility-cube",
        arg_string="--pipeline.use_visibility_loss True --pipeline.use_singlestep_cube_loss True",
    ),
    Argument(
        name="nerfacto-visibility-sparsity",
        arg_string="--pipeline.use_visibility_loss True --pipeline.use_singlestep_cube_loss False --pipeline.use_sparsity_loss True",
    ),
    Argument(
        name="nerfacto-visibility-TV",
        arg_string="--pipeline.use_visibility_loss True --pipeline.use_singlestep_cube_loss False --pipeline.use_total_variation_loss True",
    ),
    Argument(
        name="nerfacto-visibility-regnerf",
        arg_string="--pipeline.use_visibility_loss True --pipeline.use_singlestep_cube_loss False --pipeline.use_regnerf_loss True",
    )
]
arguments_list_of_lists.append(experiments_list)
