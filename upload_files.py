#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 15:06:19 2025

@author: mike
"""
# import s3func
# import concurrent.futures
import pathlib
import shlex
import subprocess

import params



############################################
### Parameters

remote = params.file['remote']


###########################################
### Functions


# def download_file(src_session, key):
#     """

#     """
#     resp = src_session.get_object(key)
#     if resp.status // 100 == 2:
#         file_name = key.split('/')[-1]
#         dl_file_path = dl_path.joinpath(file_name)
#         shutil.copyfileobj(resp.stream, open(dl_file_path, 'wb'), 2**21)
#         msg = 'success'
#     else:
#         msg = str(resp.error)

#     return msg


def create_rclone_config(data_path, access_key_id, access_key, endpoint_url, download_url=None):
    """

    """
    config_dict = {}
    if isinstance(download_url, str) or 'backblazeb2' in endpoint_url:
        type_ = 'b2'
        # config_dict['type'] = 'b2'
        config_dict['account'] = access_key_id
        config_dict['key'] = access_key
        config_dict['hard_delete'] = 'true'
        if isinstance(download_url, str):
            config_dict['download_url'] = download_url
    else:
        type_ = 's3'
        # config_dict['type'] = 's3'
        if 'mega' in endpoint_url:
            provider = 'Mega'
        else:
            provider = 'Other'
        config_dict['provider'] = provider
        config_dict['access_key_id'] = access_key_id
        config_dict['secret_access_key'] = access_key
        config_dict['endpoint'] = endpoint_url

    config_list = [f'{k}={v}' for k, v in config_dict.items()]
    config_str = ' '.join(config_list)
    config_path = data_path.joinpath('rclone.config')
    cmd_str = f'rclone config create s3 {type_} {config_str} --config={config_path} --non-interactive --obscure'
    cmd_list = shlex.split(cmd_str)
    p = subprocess.run(cmd_list, capture_output=True, text=True, check=True)

    return config_path


# def upload_file(dst_session, key, file_path):
#     """

#     """
#     resp = dst_session.put_object(key, open(file_path))
#     if resp.status // 100 == 2:
#         msg = 'success'
#     else:
#         msg = str(resp.error)

#     return msg


def upload_files():
    """

    """
    base_path = pathlib.Path(remote['base_path'])
    proj_path = base_path.joinpath(params.file['project_name'])

    access_key_id = remote['access_key_id']
    access_key = remote['access_key']
    bucket = remote['bucket']
    endpoint_url = remote['endpoint_url']

    config_path = create_rclone_config(params.data_path, access_key_id, access_key, endpoint_url)

    dst_str = f's3:{bucket}/{proj_path}/'
    cmd_str = f'rclone copy {params.data_path} {dst_str} --config={config_path} --exclude="rclone.config"'
    cmd_list = shlex.split(cmd_str)
    p = subprocess.run(cmd_list, capture_output=True, text=True, check=True)
    for file_path in params.data_path.iterdir():
        if file_path.is_file():
            file_path.unlink()
    if p.stderr != '':
        return print(p.stderr)
    else:
        return print('success')



    # dst_session = s3func.S3Session(remote['access_key_id'], remote['access_key'], remote['bucket'], remote['endpoint_url'], stream=False)



    # with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    #     futures = {}
    #     for file_path in params.data_path.iterdir():
    #         if file_path.is_file():
    #             print(file_path)
    #             key = str(proj_path.joinpath(file_path.name))
    #             f = executor.submit(upload_file, dst_session, key, file_path)
    #             futures[f] = key

    #     for future in concurrent.futures.as_completed(futures):
    #         key = futures[future]
    #         msg = future.result()
    #         if msg == 'success':
    #             print(f'success: {key}')
    #         else:
    #             print(f'failed: {key} - {msg}')


############################################
### Upload files








